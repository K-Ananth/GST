[app]
title = Calculator
package.name = calculator
package.domain = org.example
source.dir = .
source.include_exts = py
source.include_patterns = lib/**/*
source.exclude_exts = spec, yml, yaml, md
source.exclude_patterns = assets/**/*
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/lib/main.py
requirements = python3==3.10.9,kivy==2.0.0,kivymd==1.1.1,pil
source.include_patterns = data/*,lib/*
icon.filename = %(source.dir)s/data/icon.png
orientation = portrait
fullscreen = 1
