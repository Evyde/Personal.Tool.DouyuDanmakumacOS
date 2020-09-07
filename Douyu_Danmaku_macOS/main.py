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
i18n.set('fallback', "en")
i18n.set('file_format', 'yaml')
i18n.config.json_available = False
i18n.config.yaml_available = True
i18n.add_translation('foo.h', 'bar', locale='en_US')
i18n.add_translation('foo.h', '傻逼', locale='zh_CN')

i18n.load_path.append("C:\\Users\\Evyde\\PycharmProjects\\Douyu_Danmu_For_macOS\\Douyu_Danmaku_macOS")
print(i18n.t('title.a', locale='en'))
print(i18n.config.settings)
print(i18n.t('foo.h', locale='zh_CN'))

#asyncio.run(main())