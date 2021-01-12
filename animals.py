from __future__ import absolute_import, division, print_function, unicode_literals
from sopel import module
import requests


@module.commands("cat")
def cats(bot, trigger):
    """Posts a random cat using the aws.random.cat/meow API."""
    url = "https://aws.random.cat/meow"
    cat_image = requests.get(url).json()['file']
    bot.say(cat_image)


@module.commands("catgif")
def catgif(bot, trigger):
    """Posts a random cat GIF using thecatapi.com API."""
    url = "https://api.thecatapi.com/v1/images/search?mime_types=gif"
    cat_gif = requests.get(url).json()[0]['url']
    bot.say(cat_gif)


@module.commands("dog")
def dogs(bot, trigger):
    """Posts a random dog using the dog.ceo/dog-api API."""
    url = "https://dog.ceo/api/breeds/image/random"
    dog_image = requests.get(url).json()['message']
    bot.say(dog_image)


@module.commands("shibe")
def shibe(bot, trigger):
    """Posts a random Shiba Inu using the shibe.online API."""
    url = "https://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true"
    shibe_image = requests.get(url).json()[0]
    bot.say(shibe_image)


@module.commands("birb", "bird")
def birbs(bot, trigger):
    """Posts a random bird using the shibe.online bird API."""
    url = "https://shibe.online/api/birds?count=1&urls=true&httpsUrls=true"
    birb_image = requests.get(url).json()[0]
    bot.say(birb_image)


@module.commands("fox", "foxy")
def fox(bot, trigger):
    """Posts a random fox using the randomfox.ca API."""
    url = "https://randomfox.ca/floof/"
    fox_image = requests.get(url).json()['image']
    bot.say(fox_image)
