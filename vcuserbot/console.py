import os
import time
import logging

from os import getenv
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler


logging.basicConfig(
    format="[%(asctime)s]:[%(levelname)s]:[%(name)s]:: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "logs.txt", maxBytes=(1024 * 1024 * 5), backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)


if os.path.exists("Internal"):
   load_dotenv("Internal")


API_ID = int(getenv("API_ID", 0))
API_HASH = getenv("API_HASH", None)
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING_SESSION = getenv("STRING_SESSION", None)
MONGO_DB_URL = getenv("MONGO_DB_URL", None)
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", 0))


# OPTIONAL VARIABLES
SESSION_STRING = getenv("SESSION_STRING", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". !").split())



# OTHERS VARIABLES

# PM GUARD VARS
PM_GUARD = bool(getenv("PM_GUARD", True))
PM_GUARD_TEXT = getenv("PM_GUARD_TEXT", "**🥀 𝐇𝐞𝐲, 𝐈 𝐚𝐦 𝐚𝐧 𝐚𝐝𝐯𝐚𝐧𝐜𝐞𝐝 & 𝐬𝐮𝐩𝐞𝐫𝐟𝐚𝐬𝐭 𝐡𝐢𝐠𝐡 𝐪𝐮𝐚𝐥𝐢𝐭𝐲 𝐮𝐬𝐞𝐫𝐛𝐨𝐭 𝐚𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐰𝐢𝐭𝐡 𝐚𝐧 𝐮𝐩𝐠𝐫𝐚𝐝𝐞𝐝 𝐯𝐞𝐫𝐬𝐢𝐨𝐧 𝐬𝐞𝐜𝐮𝐫𝐢𝐭𝐲 𝐬𝐲𝐬𝐭𝐞𝐦.\n\n🌿 𝙄 𝙘𝙖𝙣'𝙩 𝙡𝙚𝙩 𝙮𝙤𝙪 𝙢𝙚𝙨𝙨𝙖𝙜𝙚 𝙢𝙮 𝙤𝙬𝙣𝙚𝙧'𝙨 𝙙𝙢 𝙬𝙞𝙩𝙝𝙤𝙪𝙩 𝙢𝙮 𝙤𝙬𝙣𝙚𝙧'𝙨 𝙥𝙚𝙧𝙢𝙞𝙨𝙨𝙞𝙤𝙣.\n\n🌺 ᴹʸ ᵒʷⁿᵉʳ ⁱˢ ᵒᶠᶠˡⁱⁿᵉ ⁿᵒʷ, ᵖˡᵉᵃˢᵉ ʷᵃⁱᵗ ᵘⁿᵗⁱˡ ᵐʸ ᵒʷⁿᵉʳ ᵃˡˡᵒʷˢ ʸᵒᵘ.\n\n🍂 𝐏𝐥𝐞𝐚𝐬𝐞 𝐝𝐨𝐧'𝐭 𝐬𝐩𝐚𝐦 𝐡𝐞𝐫𝐞, 𝐛𝐞𝐜𝐚𝐮𝐬𝐞 𝐬𝐩𝐚𝐦𝐦𝐢𝐧𝐠 𝐰𝐢𝐥𝐥 𝐟𝐨𝐫𝐜𝐞 𝐦𝐞 𝐭𝐨 𝐛𝐥𝐨𝐜𝐤 𝐲𝐨𝐮 𝐟𝐫𝐨𝐦 𝐦𝐲 𝐨𝐰𝐧𝐞𝐫 𝐢𝐝.**")
PM_GUARD_LIMIT = int(getenv("PM_GUARD_LIMIT", 5))



# USERBOT DEFAULT IMAGE
USERBOT_PICTURE = getenv("USERBOT_PICTURE", "https://telegra.ph/file/47c344f3e278ea9a82294.jpg")



# Don't Edit This Codes From This Line

LOGGER = logging.getLogger("vcuserbot")
runtime = time.time()

FLOODXD = {}
OLD_MSG = {}
PM_LIMIT = {}
PLUGINS = {}
SUDOERS = []


COMMAND_HANDLERS = []
for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)
COMMAND_HANDLERS.append('')

