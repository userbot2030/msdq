# ZeldrisRobot
# Copyright (C) 2017-2019, Paul Larsen
# Copyright (C) 2022, IDNCoderX Team, <https://github.com/IDN-C-X/ZeldrisRobot>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
if not __name__.endswith("sample_config"):
    import sys

    print(
        "The README is there to be read. Extend this sample config to a config file, don't just rename and change "
        "values here. Doing that WILL backfire on you.\nBot quitting.",
        file=sys.stderr,
    )
    sys.exit(1)"""


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    TOKEN = "6358776255:AAHFnLLrzlkOr8yXlHjol0QDmbyR-q2oJgc"
    OWNER_ID = (
        "1814359323"
    )
    OWNER_USERNAME = "msdqqq"
    API_HASH = "c01b59b1d686c55d60a92c171e2b19fe"
    API_ID = 29855436

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgresql://llljalfi:4ZD49HMaJsUzWTeGAIEW5dS4ID87H2DH@stampy.db.elephantsql.com/llljalfi"
    MESSAGE_DUMP = "-1001880060276"
    REDIS_URL = "redis://default:TIKFEat8Hvjuhqy3YhEmIKLDNxUBsT4u@redis-14835.c252.ap-southeast-1-1.ec2.cloud.redislabs.com:14835"
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    URL = None
    MONGO_URI = "mongodb+srv://Iam:alam@iam.1be2qw9.mongodb.net/Iam?retryWrites=true&w=majority"
    MONGO_PORT = 27017  # leave it as it is
    MONGO_DB = "Zeldris"
    BOT_USERNAME = "AmelXDzulMusicRobot"
    PICTURE = "https://telegra.ph/file/2a82d72372e52b3138e08.jpg"

    # OPTIONAL
    DEV_USERS = (
        [1814359323]
    )  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = (
        [1814359323]
    )  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = (
        [1814359323]
    )  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    WHITELIST_CHATS = []
    BLACKLIST_CHATS = []
    DONATION_LINK = "https://t.me/DezetStore"
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = None  # banhammer marie sticker
    ALLOW_EXCL = False  # DEPRECATED, USE BELOW INSTEAD! Allow ! commands as well as /
    CUSTOM_CMD = False  # Set to ('/', '!') or whatever to enable it, like ALLOW_EXCL but with more custom handler!
    API_OPENWEATHER = None  # OpenWeather API
    SPAMWATCH_API = "Ivaq3WVuTX79bw_ISy9~I3TU6MtMvldP0HgP1bpzzYaX5pKMXtyINHC61DEQpnxh"
    WALL_API = None
    SPAMMERS = None


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
