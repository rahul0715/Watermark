import asyncio
import importlib
from pyrogram import idle
from TXT.modules import ALL_MODULES
from TXT.core.database import setup_sudoers


async def sumit_boot():
    await setup_sudoers()
    for all_module in ALL_MODULES:
        importlib.import_module("TXT.modules." + all_module)

    print("» ʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ ✨ 🎉")
    await idle()
    print("» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")
    
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(sumit_boot())