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


      as status:
        console.print("┌ [red]Booting Up The Clients...\n")
        await app.start()
        console.print("└ [green]Booted Bot Client")
        console.print("\n┌ [red]Booting Up The Assistant Clients...")
        if STRING1 != "None":
            await ASS_CLI_1.start()
            random_assistant.append(1)
            console.print("├ [yellow]Booted Assistant Client")
        if STRING2 != "None":
            await ASS_CLI_2.start()
            random_assistant.append(2)
            console.print("├ [yellow]Booted Assistant Client 2")
        if STRING3 != "None":
            await ASS_CLI_3.start()
            random_assistant.append(3)
            console.print("├ [yellow]Booted Assistant Client 3")
        if STRING4 != "None":
            await ASS_CLI_4.start()
            random_assistant.append(4)
            console.print("├ [yellow]Booted Assistant Client 4")
        if STRING5 != "None":
            await ASS_CLI_5.start()
            random_assistant.append(5)
            console.print("├ [yellow]Booted Assistant Client 5")
        if STRING6 != "None":
            await ASS_CLI_6.start()
            random_assistant.append(6)
            console.print("├ [yellow]Booted Assistant Client 6")
        console.print("└ [green]Assistant Clients Booted Successfully!")


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
