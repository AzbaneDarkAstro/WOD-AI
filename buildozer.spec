[app]
title = WOD-AI
package.name = wodai
package.domain = com.azbane.wodai

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
source.include_patterns = NotoNaskhArabic.ttf

version = 1.0
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py

[buildozer]
log_level = 2

# requirements - غادي نخدمو ب kivy
requirements = python3,kivy,Pillow,arabic-reshaper,python-bidi

# orientation
orientation = portrait

# icon (الى عندك)
#icon.filename = %(source.dir)s/icon.png

[app:requirements]

[app:android]
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
# باش الفونت يخدم
android.add_resources = NotoNaskhArabic.ttf

# p4a branch
p4a.branch = master

[buildozer:android]
