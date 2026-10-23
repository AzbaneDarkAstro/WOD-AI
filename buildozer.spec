[app]
title = WOD-AI
package.name = wodai
package.domain = com.azbane.wodai
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
version = 1.0
requirements = python3,kivy==2.3.0,kivymd==1.2.0,Pillow,arabic-reshaper,python-bidi
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 0

[app:android]
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 28c
android.accept_sdk_license_agreements = True
android.sdk_build_tools_version = 34.0.0
android.archs = arm64-v8a
android.allow_backup = False

p4a.branch = master
p4a.bootstrap = sdl2
