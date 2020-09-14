import globalvars
from rumps import *


class DouyuDanmakuAppViewer(App):
    def __init__(self, **args):
        super().__init__(**args)
        isGiftNotificationMenuItem = MenuItem(globalvars.i18n.t('isGiftNotification'),
                                              callback=self.giftNotificationOnoff, key='G')
        isGiftNotificationMenuItem.state = True
        localItems = []
        for locale in globalvars.i18n.get('available_locales'):
            if locale is globalvars.i18n.get('locale'):
                nowUsingLocaleMenuItem = MenuItem(globalvars.i18n.t('lan', locale=locale), callback=self.changeLanguage)
                nowUsingLocaleMenuItem.state = True
                localItems.append(nowUsingLocaleMenuItem)
            else:
                localItems.append(MenuItem(globalvars.i18n.t('lan', locale=locale), callback=self.changeLanguage))
        self.menu = [
            globalvars.i18n.t('about'),
            None,
            [
                globalvars.i18n.t('preferences'),
                (isGiftNotificationMenuItem,
                 MenuItem(globalvars.i18n.t('inputRoomIDTitle'), callback=self.inputRoomID, key='I'),
                 [globalvars.i18n.t('languageSetting'), localItems]
                 )
            ],
            globalvars.i18n.t('start'),
            None
        ]

    def inputRoomID(self, _):
        print(Window(globalvars.i18n.t('inputRoomIDTitle'), globalvars.i18n.t('inputRoomID')).run().text)

    def giftNotificationOnoff(self, sender):
        sender.state = not sender.state
        globalvars.isGiftNotification = sender

    @clicked(globalvars.i18n.t('about'))
    def about(self, _):
        alert(globalvars.i18n.t('description', version=globalvars.version))

    @clicked(globalvars.i18n.t('start'))
    def startReceiving(self, sender):

    def changeLanguage(self, sender):
        sender.state = True
        for lanSetting in globalvars.i18n.get('available_locales'):
            if globalvars.i18n.t('languageSetting', locale=lanSetting) == sender.title:
                globalvars.log.info("Set language to %s.", sender.title)
                globalvars.cfg.set("common", "language", lanSetting)
                globalvars.i18n.set('locale', lanSetting)
                with open(globalvars.configPath) as fp:
                    globalvars.log.warn("Config file opened.")
                    globalvars.cfg.write(fp)
                # TODO: UPDATE MENU, I THINK I SHOULD DEL WHOLE MENU AND RECREATE IT
