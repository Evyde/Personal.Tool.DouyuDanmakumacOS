import asyncio
import danmaku
import rumps

async def printer(q):
    while True:
        m = await q.get()
        if m['msg_type'] == "danmaku":
            print("[%s] ：%s" % (m['name'], m['content']))


async def main():
    q = asyncio.Queue()
    roomID = int(input("输入房间号："))
    dmc = danmaku.DanmakuClient("https://douyu.com/%d" % roomID, q)
    asyncio.create_task(printer(q))
    await dmc.start()

asyncio.run(main())