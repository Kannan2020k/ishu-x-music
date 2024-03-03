from ishu.core.bot import AnonXBot
from ishu.core.dir import dirr
from ishu.core.git import git
from ishu.core.userbot import Userbot
from ishu.misc import dbb, heroku, sudo

from .logging import LOGGER


dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = ishuXBot()
userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
