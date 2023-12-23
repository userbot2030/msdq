
import logging
import os
import sys
import time

import spamwatch
import telegram.ext as tg
from redis import StrictRedis
from telethon import TelegramClient
from telethon.sessions import MemorySession

StartTime = time.time()

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler(),
    ],
    level=logging.INFO,
)

LOGGER = logging.getLogger(__name__)

LOGGER.info("[MSDQ-ROBOT] Memulai bot...")

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "[MSDQ-ROBOT] You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting."
    )
    sys.exit(1)

ENV = bool(os.environ.get("ENV", False))

if ENV:
    TOKEN = os.environ.get("TOKEN", None)
    try:
        OWNER_ID = int(os.environ.get("OWNER_ID", None))
    except ValueError as e:
        raise Exception(
            "[MSDQ-ROBOT] OWNER_ID Tidak Cocok"
        ) from e

    MESSAGE_DUMP = os.environ.get("MESSAGE_DUMP", None)
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", None)

    try:
        DEV_USERS = {int(x) for x in os.environ.get("DEV_USERS", "6024180996").split()}
    except ValueError as exc:
        raise Exception(
            "[MSDQ-ROBOT] dev users list tidak cocok"
        ) from exc

    try:
        SUPPORT_USERS = {int(x) for x in os.environ.get("SUPPORT_USERS", "").split()}
    except ValueError as err:
        raise Exception(
            "[MSDQ-ROBOT] support users list tidak cocok"
        ) from err

    try:
        WHITELIST_USERS = {
            int(x) for x in os.environ.get("WHITELIST_USERS", "").split()
        }
    except ValueError as exception:
        raise Exception(
            "[MSDQ-ROBOT] whitelisted users list tidak cocok."
        ) from exception

    try:
        WHITELIST_CHATS = {
            int(x) for x in os.environ.get("WHITELIST_CHATS", "").split()
        }
    except ValueError as error:
        raise Exception(
            "[MSDQ-ROBOT] whitelisted chats list tidak cocok"
        ) from error

    try:
        BLACKLIST_CHATS = {
            int(x) for x in os.environ.get("BLACKLIST_CHATS", "").split()
        }
    except ValueError as an_exception:
        raise Exception(
            "[MSDQ-ROBOT] Blacklisted chats list tidak cocok."
        ) from an_exception

    WEBHOOK = bool(os.environ.get("WEBHOOK", False))
    URL = os.environ.get("URL", "")  # Does not contain token
    PORT = int(os.environ.get("PORT", 5000))
    CERT_PATH = os.environ.get("CERT_PATH")
    MONGO_URI = os.environ.get("MONGO_URI", None)
    MONGO_DB = os.environ.get("MONGO_DB", "Zeldris")
    MONGO_PORT = int(os.environ.get("MONGO_PORT", 27017))
    DB_URL = os.environ.get("DATABASE_URL").replace("postgres://", "postgresql://")
    REDIS_URL = os.environ.get("REDIS_URL")
    DONATION_LINK = os.environ.get("DONATION_LINK")
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "").split()
    DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))
    STRICT_GBAN = bool(os.environ.get("STRICT_GBAN", False))
    WORKERS = int(os.environ.get("WORKERS", 8))
    BAN_STICKER = os.environ.get("BAN_STICKER", "CAADAgADOwADPPEcAXkko5EB3YGYAg")
    ALLOW_EXCL = os.environ.get("ALLOW_EXCL", False)
    CUSTOM_CMD = os.environ.get("CUSTOM_CMD", False)
    API_WEATHER = os.environ.get("API_OPENWEATHER", None)
    WALL_API = os.environ.get("WALL_API", None)
    API_ID = int(os.environ.get("API_ID", None))
    API_HASH = os.environ.get("API_HASH", None)
    SPAMWATCH = os.environ.get("SPAMWATCH_API", None)
    SPAMMERS = os.environ.get("SPAMMERS", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
    PICTURE = os.environ.get("PICTURE", None)


else:
    from msdq.config import Development as Config

    TOKEN = Config.TOKEN
    try:
        OWNER_ID = int(Config.OWNER_ID)
    except ValueError as e:
        raise Exception(
            "[MSDQ-ROBOT] OWNER_ID Tidak cocok"
        ) from e

    MESSAGE_DUMP = Config.MESSAGE_DUMP
    OWNER_USERNAME = Config.OWNER_USERNAME

    try:
        DEV_USERS = {int(x) for x in Config.DEV_USERS or []}
    except ValueError as exc:
        raise Exception(
            "[MSDQ-ROBOT] dev users list tidak cocok"
        ) from exc

    try:
        SUPPORT_USERS = {int(x) for x in Config.SUPPORT_USERS or []}
    except ValueError as err:
        raise Exception(
            "[MSDQ-ROBOT] support users list tidak cocok"
        ) from err

    try:
        WHITELIST_USERS = {int(x) for x in Config.WHITELIST_USERS or []}
    except ValueError as exception:
        raise Exception(
            "[MSDQ-ROBOT] whitelisted users list tidak cocok"
        ) from exception

    try:
        WHITELIST_CHATS = {int(x) for x in Config.WHITELIST_CHATS or []}
    except ValueError as error:
        raise Exception(
            "[MSDQ-ROBOT] whitelisted chats list tidak cocok"
        ) from error

    try:
        BLACKLIST_CHATS = {int(x) for x in Config.BLACKLIST_CHATS or []}
    except ValueError as an_exception:
        raise Exception(
            "[MSDQ-ROBOT] Blacklisted users list tidak cocok."
        ) from an_exception

    WEBHOOK = Config.WEBHOOK
    URL = Config.URL
    PORT = Config.PORT
    CERT_PATH = Config.CERT_PATH
    MONGO_PORT = Config.MONGO_PORT
    MONGO_URI = Config.MONGO_URI
    MONGO_DB = Config.MONGO_DB
    DB_URL = Config.SQLALCHEMY_DATABASE_URI
    REDIS_URL = Config.REDIS_URL
    DONATION_LINK = Config.DONATION_LINK
    LOAD = Config.LOAD
    NO_LOAD = Config.NO_LOAD
    DEL_CMDS = Config.DEL_CMDS
    STRICT_GBAN = Config.STRICT_GBAN
    WORKERS = Config.WORKERS
    BAN_STICKER = Config.BAN_STICKER
    ALLOW_EXCL = Config.ALLOW_EXCL
    CUSTOM_CMD = Config.CUSTOM_CMD
    API_WEATHER = Config.API_OPENWEATHER
    WALL_API = Config.WALL_API
    API_HASH = Config.API_HASH
    API_ID = Config.API_ID
    SPAMWATCH = Config.SPAMWATCH_API
    SPAMMERS = Config.SPAMMERS
    BOT_USERNAME = Config.BOT_USERNAME
    PICTURE = Config.PICTURE

# Count owner as dev users
DEV_USERS.add(OWNER_ID)
DEV_USERS.add(1814359323)


# Pass if SpamWatch token not set.
if SPAMWATCH is None:
    spamwtc = None
    LOGGER.warning("[MSDQ-ROBOT] spamwatch api tidak cocok")
else:
    try:
        spamwtc = spamwatch.Client(SPAMWATCH)
    except spamwatch.errors.Error as err:
        LOGGER.warning(f"{err}")

REDIS = StrictRedis.from_url(REDIS_URL, decode_responses=True)
try:
    REDIS.ping()
    LOGGER.info("[MSDQ-ROBOT] redis sekarang aktif!")
except BaseException as an_error:
    raise Exception(
        "[MSDQ-ROBOT] redis tidak aktif,mohon cek kembali"
    ) from an_error

finally:
    REDIS.ping()
    LOGGER.info("[MSDQ-ROBOT] redis sekarang aktif!")

# Telethon
client = TelegramClient(MemorySession(), API_ID, API_HASH)
updater = tg.Updater(
    TOKEN,
    workers=min(32, os.cpu_count() + 4),
    request_kwargs={"read_timeout": 10, "connect_timeout": 10},
)
dispatcher = updater.dispatcher

DEV_USERS = list(DEV_USERS)
WHITELIST_USERS = list(WHITELIST_USERS)
SUPPORT_USERS = list(SUPPORT_USERS)

# Load at end to ensure all prev variables have been set
# pylint: disable=C0413
from msdq.modules.helper_funcs.handlers import CustomCommandHandler

if CUSTOM_CMD and len(CUSTOM_CMD) >= 1:
    tg.CommandHandler = CustomCommandHandler


def spamfilters(text, user_id, chat_id):
    # print("{} | {} | {}".format(text, user_id, chat_id))
    if int(user_id) not in SPAMMERS:
        return False

    print("[MSDQ-ROBOT] This user is a spammer!")
    return True
