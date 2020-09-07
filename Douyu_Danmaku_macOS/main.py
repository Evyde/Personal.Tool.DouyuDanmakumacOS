import asyncio
import danmaku
#import rumps
#import esky
#import py2app
import i18n
import os


async def printer(q):
    while True:
        m = await q.get()
        if m['msg_type'] == "danmaku":
            print("[%s] ：%s" % (m['name'], m['content']))


async def main():
    q = asyncio.Queue()
    roomID = int(input(i18n.t('title.a')))
    dmc = danmaku.DanmakuClient("https://douyu.com/%d" % roomID, q)
    asyncio.create_task(printer(q))
    await dmc.start()
i18n.set('available_locales', ['en_US', 'zh_CN', 'en'])
i18n.set('locale', 'en')
i18n.set('fallback', "en_US")

i18n.load_path.append("Douyu_Danmaku_macOS/i18n")
print(i18n.t('en.title.a', locale='en_US'))

asyncio.run(main())