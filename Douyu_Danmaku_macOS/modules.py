import asyncio
import time

import danmaku
import i18n
import globalvars, threading, views
import configparser
import logging as log


# This class should have only single instance
# TODO: SINGLE INSTANCE CHECK
class DanmakuGetter:
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
        global app
        q = asyncio.Queue()
        roomID = int(input(i18n.t('inputRoomID')))
        dmc = danmaku.DanmakuClient("https://douyu.com/%d" % roomID, q)
        asyncio.create_task(self.printer(q))
        await dmc.start()


def init():
    # Configure i18n
    # TODO: I18N SHOULD SHARE AS GLOBAL
    globalvars.i18n.set('available_locales', ['en_US', 'zh_CN'])
    globalvars.i18n.set('locale', globalvars.lan)
    globalvars.i18n.set('fallback', "en_US")
    globalvars.i18n.set('file_format', 'yaml')
    globalvars.i18n.set('filename_format', '{locale}.{format}')
    globalvars.i18n.load_path.append(globalvars.i18nPath)

    # Configure log
    # Remember to change `log.DEBUG` to INFO or something.
    log.basicConfig(filename=globalvars.logPath, level=log.DEBUG)

    # Configure config.ini
    cfg = configparser.ConfigParser()
    cfg.read(globalvars.configPath, encoding="utf-8")

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
