from pathlib import Path

from kivy.app import App
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.text import LabelBase
from kivy.graphics import Color, RoundedRectangle
from kivy.clock import Clock

# دعم تشكيل الحروف العربية إن كانت المكتبات مثبتة
try:
    import arabic_reshaper
    from bidi.algorithm import get_display

    def arabic(text):
        return get_display(arabic_reshaper.reshape(text))

except ImportError:
    def arabic(text):
        return text

# الألوان
BG = (0.035, 0.02, 0.07, 1)
PURPLE = (0.48, 0.20, 0.85, 1)
PANEL = (0.10, 0.065, 0.15, 1)
WHITE = (1, 1, 1, 1)
MUTED = (0.72, 0.66, 0.82, 1)

Window.clearcolor = BG

# تحميل الخط العربي من مجلد المشروع
FONT = "Roboto"


font_file = Path(__file__).parent / "NotoNaskhArabic.ttf"




if font_file.exists():
    LabelBase.register(
        name="WODArabic",
        fn_regular=str(font_file)
    )
    FONT = "WODArabic"


def make_label(text, **kwargs):
    kwargs.setdefault("font_name", FONT)
    return Label(text=text, **kwargs)


class Message(BoxLayout):
    def __init__(self, text, user=False, **kwargs):
        super().__init__(
            orientation="vertical",
            size_hint_y=None,
            padding=dp(12),
            spacing=dp(5),
            **kwargs
        )

        self.bind(minimum_height=self.setter("height"))

        with self.canvas.before:
            Color(*(PURPLE if user else PANEL))
            self.rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(15)]
            )

        self.bind(pos=self.update_rect, size=self.update_rect)

        title = make_label(
            arabic("أنت" if user else "WOD AI"),
            size_hint_y=None,
            height=dp(28),
            color=(0.88, 0.72, 1, 1),
            bold=True,
            font_size="16sp",
            halign="right",
            valign="middle"
        )

        title.bind(
            size=lambda obj, val:
            setattr(obj, "text_size", val)
        )

        body = make_label(
            arabic(text),
            size_hint_y=None,
            color=WHITE,
            font_size="17sp",
            halign="right",
            valign="top"
        )

        body.bind(
            width=lambda obj, val:
            setattr(obj, "text_size", (max(1, val), None)),
            texture_size=lambda obj, val:
            setattr(obj, "height", val[1] + dp(12))
        )

        self.add_widget(title)
        self.add_widget(body)

    def update_rect(self, *_):
        self.rect.pos = self.pos
        self.rect.size = self.size


class WODAI(App):
    title = "WOD AI"

    def build(self):
        root = BoxLayout(
            orientation="vertical",
            padding=dp(14),
            spacing=dp(10)
        )

        # رأس التطبيق
        header = BoxLayout(
            size_hint_y=None,
            height=dp(78),
            spacing=dp(10)
        )

        logo = Label(
            text="✦",
            color=(0.8, 0.55, 1, 1),
            font_size="42sp",
            size_hint_x=None,
            width=dp(55)
        )

        brand = BoxLayout(orientation="vertical")

        brand.add_widget(Label(
            text="[b]WOD AI[/b]",
            markup=True,
            color=WHITE,
            font_size="27sp",
            halign="left",
            valign="middle"
        ))

        brand.add_widget(Label(
            text="YOUR INTELLIGENT ASSISTANT",
            color=MUTED,
            font_size="10sp",
            halign="left",
            valign="middle"
        ))

        header.add_widget(logo)
        header.add_widget(brand)
        root.add_widget(header)

        # المحادثة
        self.scroll = ScrollView(
            do_scroll_x=False,
            bar_width=dp(3)
        )

        self.messages = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            spacing=dp(12),
            padding=(0, dp(8))
        )

        self.messages.bind(
            minimum_height=self.messages.setter("height")
        )

        self.scroll.add_widget(self.messages)
        root.add_widget(self.scroll)

        self.add_message(
            "مرحباً بك في WOD AI! 💜\n"
            "أنا مساعدك الذكي. كيف أستطيع مساعدتك اليوم؟"
        )

        # أسئلة سريعة
        quick = BoxLayout(
            size_hint_y=None,
            height=dp(44),
            spacing=dp(6)
        )

        questions = [
            ("مساعدة", "كيف يمكنك مساعدتي؟"),
            ("Python", "علمني أساسيات Python"),
            ("أفكار", "اقترح أفكاراً لمشروعي")
        ]

        for caption, question in questions:
            btn = Button(
                text=arabic(caption),
                font_name=FONT,
                font_size="13sp",
                background_normal="",
                background_color=PANEL,
                color=WHITE
            )
            btn.bind(
                on_release=lambda instance, q=question:
                self.quick_send(q)
            )
            quick.add_widget(btn)

        root.add_widget(quick)

        # خانة الرسالة
        composer = BoxLayout(
            size_hint_y=None,
            height=dp(58),
            spacing=dp(8)
        )

        self.input = TextInput(
            hint_text=arabic("اكتب رسالتك هنا..."),
            font_name=FONT,
            multiline=False,
            font_size="16sp",
            foreground_color=WHITE,
            hint_text_color=MUTED,
            cursor_color=(0.8, 0.5, 1, 1),
            background_normal="",
            background_active="",
            background_color=PANEL,
            padding=[dp(12), dp(16), dp(12), dp(10)]
        )

        self.input.bind(on_text_validate=self.send_message)

        send = Button(
            text="➤",
            size_hint_x=None,
            width=dp(60),
            font_size="25sp",
            background_normal="",
            background_color=PURPLE,
            color=WHITE
        )

        send.bind(on_release=self.send_message)

        composer.add_widget(self.input)
        composer.add_widget(send)
        root.add_widget(composer)

        root.add_widget(make_label(
            arabic("WOD AI • النسخة التجريبية"),
            size_hint_y=None,
            height=dp(24),
            color=MUTED,
            font_size="11sp"
        ))

        return root

    def add_message(self, text, user=False):
        bubble = Message(
            text,
            user=user,
            size_hint_x=0.96
        )

        bubble.pos_hint = (
            {"right": 1} if user else {"x": 0}
        )

        self.messages.add_widget(bubble)

        Clock.schedule_once(
            lambda dt: setattr(self.scroll, "scroll_y", 0),
            0.2
        )

    def quick_send(self, question):
        self.input.text = arabic(question)
        self.send_message()

    def send_message(self, *_):
        text = self.input.text.strip()

        if not text:
            return

        # إعادة تشكيل النص المعروض في خانة الكتابة
        # ليست مطلوبة هنا؛ نحتفظ بالنص الأصلي للإجابة.
        self.add_message(text, user=True)
        self.input.text = ""

        normalized = text.lower()

        if any(w in normalized for w in
               ["سلام", "مرحبا", "مرحباً", "السلام"]):
            reply = "وعليكم السلام! 💜 أهلاً بك في WOD AI."

        elif any(w in normalized for w in
                 ["python", "بايثون", "برمجة"]):
            reply = (
                "رائع! 🐍\n"
                "بايثون لغة برمجة سهلة للمبتدئين. "
                "يمكنك استخدامها لصنع التطبيقات والألعاب."
            )

        elif any(w in normalized for w in
                 ["اسمك", "من أنت", "من انت"]):
            reply = (
                "أنا WOD AI، مساعدك التجريبي. "
                "سنربطني لاحقاً بنموذج ذكاء اصطناعي حقيقي."
            )

        else:
            reply = (
                "وصلني سؤالك! 💜\n"
                "هذه نسخة تجريبية تستخدم ردوداً محلية. "
                "لم يتم ربط الذكاء الاصطناعي الحقيقي بعد."
            )

        Clock.schedule_once(
            lambda dt: self.add_message(reply),
            0.3
        )


if __name__ == "__main__":
    WODAI().run()
