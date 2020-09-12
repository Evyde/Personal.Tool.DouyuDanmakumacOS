import rumps
import globalvars


# TODO: ADD AN INTERFACE TO ALLOW USER SET THEIR ROOMID
# TODO: ADD A FUNCTION: WHEN USER CLICK STATUS BAR, STOP RECEIVING DANMAKU
class DouyuDanmakuAppViewer(rumps.App):
    def __init__(self, **args):
        super().__init__(**args)


    @rumps.clicked(globalvars.i18n.t('preferences'))
    def prefs(self, _):
        rumps.Window("输入房间号", globalvars.i18n.t('inputRoomID')).run()

    @rumps.clicked(globalvars.i18n.t('isGiftNotification'))
    def giftNotificationOnoff(self, sender):
        sender.state = not sender.state
        globalvars.isGiftNotification = sender

    @rumps.clicked(globalvars.i18n.t('about'))
    def sayhi(self, _):
        rumps.alert(globalvars.i18n.t('description', version=globalvars.version))

    @rumps.clicked('Animal', 'Dog', 'Corgi')
    def corgi_button(self, sender):
        print(sender)
        print(globalvars.i18n.t('about'))