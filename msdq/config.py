
class Config(object):
    LOGGER = True

    # WAJIB
    TOKEN = ""
    OWNER_ID = (
        "6024180996"
    )
    OWNER_USERNAME = "foundermidnight"
    API_HASH = ""
    API_ID = 

    # PRIORITAS
    SQLALCHEMY_DATABASE_URI = ""
    MESSAGE_DUMP = "-1002049500040"
    REDIS_URL = ""
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    URL = None
    MONGO_URI = ""
    MONGO_PORT = 27017  # leave it as it is
    MONGO_DB = ""
    BOT_USERNAME = ""
    PICTURE = ""

    # OPTIONAL
    DEV_USERS = (
        [6024180996]
    )  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = (
        [6024180996]
    )  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = (
        [6024180996]
    )  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    WHITELIST_CHATS = []
    BLACKLIST_CHATS = []
    DONATION_LINK = "https://t.me/Foundermidnight"
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = None  # banhammer marie sticker
    ALLOW_EXCL = False  # DEPRECATED, USE BELOW INSTEAD! Allow ! commands as well as /
    CUSTOM_CMD = False  # Set to ('/', '!') or whatever to enable it, like ALLOW_EXCL but with more custom handler!
    API_OPENWEATHER = None  # OpenWeather API
    SPAMWATCH_API = "UvVoGCq~EZaGZnIXubnELN_sDNP7fxahvT9I2eIfdXniJ6qzyj27Jbn3s18cmS3P"
    WALL_API = None
    SPAMMERS = None


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
