[app]
title = WOD-AI
package.name = wodai
package.domain = com.azbane.wodai

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
source.include_patterns = NotoNaskhArabic.ttf

version = 1.0
#version.regex = __version__ = ["'](.*)["']
#version.filename = %(source.dir)s/main.py

[buildozer]
log_level = 2
warn_on_root = 1

requirements = python3,kivy==2.3.0,kivymd,Pillow,arabic-reshaper,python-bidi

# orientation
orientation = portrait

# icon (الغيه دابا)
#icon.filename = %(source.dir)s/icon.png

[app:requirements]

[app:android]
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
android.add_resources = NotoNaskhArabic.ttf
android.ant = auto

# p4a branch - خليه خاوي
# p4a.branch = master

[buildozer:android]
