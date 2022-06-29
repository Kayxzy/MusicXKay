from PrimeMusic.core.bot import PrimeBot
from PrimeMusic.core.dir import dirr
from PrimeMusic.core.git import git
from PrimeMusic.core.userbot import Userbot
from PrimeMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = PrimeBot()

from aiohttp import ClientSession

# Assistant Client
userbot = Userbot()
ASS_CLI_1 = ASS_CLI_1
ASS_CLI_2 = ASS_CLI_2
ASS_CLI_3 = ASS_CLI_3
ASS_CLI_4 = ASS_CLI_4
ASS_CLI_5 = ASS_CLI_5
ASS_CLI_6 = ASS_CLI_6
LOG_CLIENT = LOG_CLIENT
aiohttpsession = ClientSession()
random_assistant = []


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
