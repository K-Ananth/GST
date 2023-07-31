[app]
title = QuickGST
package.name = quickgst
package.domain = org.test
source.dir = .
source.exclude_exts = spec
source.include_patterns = assets/*,images/*,fonts/*
version = 1.0.0
requirements = python3==3.10.9,kivy==2.0.0,kivymd==1.1.1,pil
orientation = portrait
android.sdk_build_tools = 29.0.3
android.api = 31
android.minapi = 21
android.arch = arm64-v8a
android.permissions = INTERNET
android.copy_libs = 1
android.archs = armeabi-v7a


[buildozer]
log_level = 2
warn_on_root = 1
