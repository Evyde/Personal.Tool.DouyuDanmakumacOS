from rumps import *
import globalvars


# TODO: ADD AN INTERFACE TO ALLOW USER SET THEIR ROOMID
# TODO: ADD A FUNCTION: WHEN USER CLICK STATUS BAR, STOP RECEIVING DANMAKU
class DouyuDanmakuAppViewer(App):
    def __init__(self, **args):
        super().__init__(**args)
        isGiftNotificationMenuItem = MenuItem(globalvars.i18n.t('isGiftNotification'), callback=self.giftNotificationOnoff, key='G')
        isGiftNotificationMenuItem.state = True
        self.menu = [
            globalvars.i18n.t('about'),
            None,
            [
                globalvars.i18n.t('preferences'),
                        (isGiftNotificationMenuItem,
                        MenuItem(globalvars.i18n.t('inputRoomIDTitle'), callback=self.inputRoomID, key='I')
                        )
            ],
            None
        ]


    def inputRoomID(self, _):
        print(rumps.Window(globalvars.i18n.t('inputRoomIDTitle'), globalvars.i18n.t('inputRoomID')).run().text)


    def giftNotificationOnoff(self, sender):
        sender.state = not sender.state
        globalvars.isGiftNotification = sender

    @clicked(globalvars.i18n.t('about'))
    def sayhi(self, _):
        rumps.alert(globalvars.i18n.t('description', version=globalvars.version))
