[app]

# (str) Title of your application
title = QuickGST

# (str) Package name
package.name = quickgst

# (str) Package domain (needed for android/ios packaging)
package.domain = org.yourdomain

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py

# (list) Source files to include (let empty to include all the files)
source.include_patterns = data/*, lib/*

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec, yml, yaml, md

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_patterns = assets/*, .git/*, __pycache__/*

# (str) Application versioning (method 1)
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py

# (str) Application versioning (method 2)
# version = 1.2.0

# (list) Application requirements
requirements = python3==3.10.9,kivy==2.0.0,kivymd==1.1.1,pil

# (bool) Use the Renpy-SDL2 instead of the default pygame provider
# sdl2 = 1

# (str) Application icon
icon.filename = %(source.dir)s/data/icon.png

# (str) Application orientation
orientation = portrait

# (list) Permissions
# android.permissions = INTERNET

# (list) Application features (adds uses-feature -tags to manifest)
# android.features = android.hardware.usb.host

# (int) Target Android API, should be as high as possible.
android.api = 27

# (int) Minimum Android API
android.minapi = 21

# (int) Android NDK version to use
android.ndk = 23.0.7599858

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android Gradle dependencies
# android.gradle_dependencies = 'com.example:pluginname:0.1'

# (str) Android Gradle repositories
# android.gradle_repositories = maven { url "https://url.to/repository" }

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# android.add_jars = foo.jar,bar.jar

# (list) List of Java files to add to the android project (can be java or kotlin)
# android.add_src = src/foo/bar/MyJava.java

# (bool) Use --log and --debug (install with python -m pip install cython)
# android.debug = False

# (str) Python/Java (legacy) dependencies to copy to libs directory
# android.copy_libs = no

# (str) Android Gradle build values to inject a custom property
# android.gradle_build_values = maxSdkVersion=28

# (bool) Enable Logcat logging from python
# android.logcat = False

# (str) Android packaging mode
# android.arch = armeabi-v7a

# (str) Android logcat filters to use
# android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
# android.copy_libs = 1

[buildozer]
log_level = 2
warn_on_root = 1
