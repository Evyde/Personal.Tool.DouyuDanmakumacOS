import globalvars
from rumps import *


class DouyuDanmakuAppViewer(App):
    def __init__(self, **args):
        super().__init__(**args)
        isGiftNotificationMenuItem = MenuItem(globalvars.i18n.t('isGiftNotification'),
                                              callback=self.giftNotificationOnoff, key='G')
        isGiftNotificationMenuItem.state = True
        # TODO: ADD AN INTERFACE TO ALLOW USER CHANGE LANGUAGE
        localItems = []
        for locale in globalvars.i18n.settings['available_locales']:
            localItems.append(MenuItem(globalvars.i18n.t('lan', locale=locale), callback=self.sender))
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

    def changeLanguage(self, sender):
        print(sender.title)
