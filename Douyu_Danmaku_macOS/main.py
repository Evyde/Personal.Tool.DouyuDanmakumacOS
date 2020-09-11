import asyncio
import threading

# import esky
# import py2app
import i18n, locale

import modules, views
import globalvars

# Get system language
if "en" in locale.getdefaultlocale()[0]:
    globalvars.lan = "en_US"
else:
    globalvars.lan = locale.getdefaultlocale()[0]

modules.init()