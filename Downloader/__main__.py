import asyncio
import importlib
from pyrogram import idle
from Downloader.modules import ALL_MODULES
from Downloader.modules.sudoers import setup_sudoers

async def sumit_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("Downloader.modules." + all_module)

    await setup_sudoers()
    print("» ʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ ✨ 🎉")
    await idle()
    print("» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")
    
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(sumit_boot())
