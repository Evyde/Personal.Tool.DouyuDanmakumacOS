import asyncio
import danmaku
import rumps
#import esky
#import py2app
import i18n
import os
import logging

version = "v0.0.1"

#rumps.App.run()
async def printer(q):
    while True:
        m = await q.get()
        if m['msg_type'] == "danmaku":
            if len(m['content']) >= 15:
                rumps.notification()
            print("[%s] ：%s" % (m['name'], m['content']))
        elif m['msg_type'] == "gift":
            rumps.notification("[%s] : %s" % (m['name'], i18n.t('sendToYouGifts')))


async def main():
    q = asyncio.Queue()
    roomID = int(input(i18n.t('inputRoomID')))
    dmc = danmaku.DanmakuClient("https://douyu.com/%d" % roomID, q)
    asyncio.create_task(printer(q))
    await dmc.start()
i18n.set('available_locales', ['en_US', 'zh_CN'])
i18n.set('locale', 'zh_CN')
i18n.set('fallback', "en_US")
i18n.set('file_format', 'yaml')
i18n.set('filename_format', '{locale}.{format}')
i18n.load_path.append("./i18n")
print(i18n.t('description', version=version))
print(i18n.t('name'))

#asyncio.run(main())