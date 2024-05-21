import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from ishu import LOGGER, app, userbot
from ishu.core.call import Anon
from ishu.plugins import ALL_MODULES
from ishu.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("ishu.plugins." + all_module)
    LOGGER("ishu.plugins").info(
        "Necessary ˹ɪꜱʜᴜ ✘ ᴍᴜꜱɪᴄ˼ ~🎵 Modules Imported Successfully."
    )
    await userbot.start()
    await Anon.start()
    try:
        await Anon.stream_call(
            "https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("ishu").error(
            "[ERROR] - \n\nHey Baby, firstly open telegram and turn on voice chat in Logger Group else fu*k off. If you ever ended voice chat in log group i will stop working and users will fu*k you up."
        )
        sys.exit()
    except:
        pass
    await Anon.decorators()
    LOGGER("ishu").info("\x41\x6E\x69\x65\x58\x45\x72\x69\x63\x61\x20\x4D\x75\x73\x69\x63\x20\x42\x6F\x74\x20\x53\x74\x61\x72\x74\x65\x64\x20\x53\x75\x63\x63\x65\x73\x73\x66\x75\x6C\x6C\x79\x2E\x5C\x6E\x5C\x6E\x44\x6F\x6E\x27\x74\x20\x66\x6F\x72\x67\x65\x74\x20\x74\x6F\x20\x4A\x6F\x69\x6E\x20\x40\x41\x4D\x42\x4F\x54\x59\x54")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("ishu").info("Stopping Music Bot...")
