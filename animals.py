from sopel import module
import requests


@module.commands("cat")
def cats(bot, trigger):
    """Posts a random cat using the aws.random.cat/meow API."""
    url = "https://aws.random.cat/meow"
    try:
        cat_image = requests.get(url).json()['file']
        bot.say(cat_image)
    except:
        bot.reply("Error reaching API, probably.")


@module.commands("catfact")
def catfact(bot, trigger):
    """Posts a random cat fact."""
    url = "https://cat-fact.herokuapp.com/facts/random"
    params = {
        "animal_type": "cat",
        "amount": "1"
    }
    try:
        cat_fact = requests.get(url, params=params).json()['text']
        bot.say(cat_fact)
    except:
        bot.reply("Error reaching API, probably.")


@module.commands("catgif")
def catgif(bot, trigger):
    """Posts a random cat GIF using thecatapi.com API."""
    url = "https://api.thecatapi.com/v1/images/search"
    params = {"mime_types": "gif"}
    try:
        cat_gif = requests.get(url, params=params).json()[0]['url']
        bot.say(cat_gif)
    except:
        bot.reply("Error reaching API, probably.")


@module.commands("dog")
def dogs(bot, trigger):
    """Posts a random dog using the dog.ceo/dog-api API."""
    url = "https://dog.ceo/api/breeds/image/random"
    try:
        dog_image = requests.get(url).json()['message']
        bot.say(dog_image)
    except:
        bot.reply("Error reaching API, probably.")


@module.commands("dogfact")
def dogfact(bot, trigger):
    """Posts a random dog fact."""
    url = "https://dog-facts-api.herokuapp.com/api/v1/resources/dogs"
    params = {"number": "1"}
    try:
        dog_fact = requests.get(url, params=params).json()[0]['fact']
        bot.say(dog_fact)
    except:
        bot.reply("Error reaching API, probably.")


@module.commands("shibe")
def shibe(bot, trigger):
    """Posts a random Shiba Inu using the shibe.online API."""
    url = "https://shibe.online/api/shibes"
    params = {
        "count": "1",
        "urls": "true",
        "httpsUrls": "true"
    }
    try:
        shibe_image = requests.get(url, params=params).json()[0]
        bot.say(shibe_image)
    except:
        bot.reply("Error reaching API, probably.")


@module.commands("birb", "bird")
def birbs(bot, trigger):
    """Posts a random bird using the shibe.online bird API."""
    url = "https://shibe.online/api/birds"
    params = {
        "count": "1",
        "urls": "true",
        "httpsUrls": "true"
    }
    try:
        birb_image = requests.get(url, params=params).json()[0]
        bot.say(birb_image)
    except:
        bot.reply("Error reaching API, probably.")


@module.commands("fox", "foxy")
def fox(bot, trigger):
    """Posts a random fox using the randomfox.ca API."""
    url = "https://randomfox.ca/floof/"
    try:
        fox_image = requests.get(url).json()['image']
        bot.say(fox_image)
    except:
        bot.reply("Error reaching API, probably.")
