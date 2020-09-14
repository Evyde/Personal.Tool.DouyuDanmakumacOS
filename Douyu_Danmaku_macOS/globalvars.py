import i18n
import logging as log
# Static vars
version = "v0.0.1"
app = None
i18nPath = "i18n"
iconPath = "icon.ico"
configPath = "config.ini"
logPath = "danmaku.log"
cfg = None
availableLocales = ['en_US', 'zh_CN']

# Variable vars (should read from config file)
lan = "zh_CN"
isGiftNotification = False