import rumps, i18n
import globalvars


# TODO: ADD AN INTERFACE TO ALLOW USER SET THEIR ROOMID
# TODO: ADD A FUNCTION: WHEN USER CLICK STATUS BAR, STOP RECEIVING DANMAKU
class DouyuDanmakuAppViewer(rumps.App):
    @rumps.clicked("Preferences")
    def prefs(self, _):
        pass

    @rumps.clicked(globalvars.i18n.t('isGiftNotification'))
    def onoff(self, sender):
        print(sender)
        print(sender.state)
        sender.state = not sender.state

    @rumps.clicked(globalvars.i18n.t('about'))
    def sayhi(self, _):
        rumps.alert(globalvars.i18n.t('description', version=globalvars.version))

    @rumps.clicked('Animal', 'Dog', 'Corgi')
    def corgi_button(self, sender):
        print(sender)