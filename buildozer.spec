[app]
title = WOD-AI
package.name = wodai
package.domain = com.azbane.wodai
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
version = 1.0
requirements = python3,kivy==2.3.0,kivymd,Pillow,arabic-reshaper,python-bidi
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
android.archs = arm64-v8a, armeabi-v7a
p4a.branch = master
p4a.bootstrap = sdl2
