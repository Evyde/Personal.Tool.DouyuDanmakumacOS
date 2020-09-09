import rumps, i18n
import globalvars


# TODO: ADD AN INTERFACE TO ALLOW USER SET THEIR ROOMID
# TODO: ADD
class DouyuDanmakuAppViewer(rumps.App):
    @rumps.clicked("Preferences")
    def prefs(self, _):
        pass

    @rumps.clicked("Silly button")
    def onoff(self, sender):
        sender.state = not sender.state

    @rumps.clicked(i18n.t('about'))
    def sayhi(self, _):
        rumps.alert(i18n.t('description', version=globalvars.version))