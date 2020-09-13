import rumps.rumps
import globalvars


# TODO: ADD AN INTERFACE TO ALLOW USER SET THEIR ROOMID
# TODO: ADD A FUNCTION: WHEN USER CLICK STATUS BAR, STOP RECEIVING DANMAKU
class DouyuDanmakuAppViewer(App):
    def __init__(self, **args):
        super().__init__(**args)
        self.menu = [
            [
                globalvars.i18n.t('preferences'), (MenuItem(globalvars.i18n.t('isGiftNotification'), key='G'),
                                                   MenuItem(globalvars.i18n.t('inputRoomIDTitle', key='I'))
                                                   )
            ],
            None,
            globalvars.i18n.t('about'),
            None
        ]


    @clicked(globalvars.i18n.t('preferences'))
    def prefs(self, _):
        print(rumps.Window(globalvars.i18n.t('inputRoomIDTitle'), globalvars.i18n.t('inputRoomID')).run())

    @clicked(globalvars.i18n.t('isGiftNotification'))
    def giftNotificationOnoff(self, sender):
        sender.state = not sender.state
        globalvars.isGiftNotification = sender

    @clicked(globalvars.i18n.t('about'))
    def sayhi(self, _):
        rumps.alert(globalvars.i18n.t('description', version=globalvars.version))

    @clicked('Animal', 'Dog', 'Corgi')
    def corgi_button(self, sender):
        print(sender)
        print(globalvars.i18n.t('about'))