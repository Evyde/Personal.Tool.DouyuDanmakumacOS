import asyncio
import time, locale

import danmaku
import i18n
import globalvars, threading
import configparser


# This class should have only single instance
# TODO: SINGLE INSTANCE CHECK
class DanmakuGetter:
    __roomID = 0

    def startLoop(self, loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()

    async def printer(self, q):
        global danmakuList, app
        while True:
            m = await q.get()
            if m['msg_type'] == "danmaku":
                if len(danmakuList) >= 5000:
                    danmakuList = []
                danmakuList.append("[%s] ：%s" % (m['name'], m['content']))
                app.title = danmakuList[len(danmakuList) - 1]
            elif m['msg_type'] == "gift":
                app.notification("%s" % i18n.t('giftNotification'), "",
                                 "[%s] : %s" % (m['name'], i18n.t('sendToYouGifts')))
                time.sleep(0.5)

    async def mainLoop(self):
        q = asyncio.Queue()
        dmc = danmaku.DanmakuClient("https://douyu.com/%d" % self.__roomID, q)
        asyncio.create_task(self.printer(q))
        await dmc.start()


def init():
    # Configure log
    # Remember to change `log.DEBUG` to INFO or something.
    globalvars.log.basicConfig(filename=globalvars.logPath, level=log.DEBUG)
    globalvars.log.info("Start running.")
    globalvars.log.info("Logging config complete.")

    # Configure config.ini
    globalvars.cfg = configparser.ConfigParser()
    globalvars.cfg.read(globalvars.configPath, encoding="utf-8")
    globalvars.log.info("Config loaded.")
    configLan = globalvars.cfg.get("common", "lan")
    if configLan == "default":
        globalvars.log.warning("Language not set, set from system.")
        if "en" in locale.getdefaultlocale()[0]:
            configLan = "en_US"
        else:
            configLan = locale.getdefaultlocale()[0]
    globalvars.lan = configLan

    # Configure i18n
    globalvars.log.info("Language set to: %s" % globalvars.lan)
    globalvars.i18n.set('available_locales', globalvars.availableLocales)
    globalvars.i18n.set('locale', globalvars.lan)
    globalvars.i18n.set('fallback', "en_US")
    globalvars.i18n.set('file_format', 'yaml')
    globalvars.i18n.set('filename_format', '{locale}.{format}')
    globalvars.i18n.load_path.append(globalvars.i18nPath)

    # Import views now because of global i18n
    import views
    app = views.DouyuDanmakuAppViewer(name=globalvars.i18n.t('name'),
                                title=globalvars.i18n.t('title'),
                                # icon=iconPath,
                                quit_button=globalvars.i18n.t('quit'))
    app.title = globalvars.i18n.t('name')
    getter = DanmakuGetter()
    con = getter.mainLoop()
    newLoop = asyncio.new_event_loop()
    t = threading.Thread(target=getter.startLoop, args=(newLoop,))
    t.setDaemon(False)
    t.start()
    asyncio.run_coroutine_threadsafe(con, newLoop)
    app.run()
