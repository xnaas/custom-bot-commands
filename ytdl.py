from __future__ import absolute_import, division, print_function, unicode_literals
from sopel import module, tools
import os
import re
import youtube_dl


ytdl_opts = {
    "format": "bestvideo[height<=?1080]+bestaudio/best",
    "merge_output_format": "mp4",
    "noplaylist": True,
    "forcejson": True,
    "outtmpl": "/mnt/media/websites/actionsack.com/tmp/%(id)s.%(ext)s"
}


@module.commands("ytdl")
def ytdl(bot, trigger):
    """Uses youtube-dl to download a video and post it to chat."""
    url = trigger.group(3)

    if not url:
        bot.reply("I need a link, silly!")
        return
    url = tools.Identifier(url)

    try:
        with youtube_dl.YoutubeDL(ytdl_opts) as ytdl:
            meta = ytdl.extract_info(url, download=False)
            id = meta["id"]
            ext = meta["ext"]
            dur = meta["duration"]
            if not dur:
                bot.reply(
                    "This video has no duration (livestream?) and cannot be downloaded.")
                return
            if dur > 600:
                bot.reply(
                    "This video is longer than 10 minutes and cannot be download, sorry!")
                return
            else:
                ytdl.download([url])
                bot.say("https://actionsack.com/tmp/{}.{}".format(id, ext))
                return
    except youtube_dl.utils.DownloadError:
        bot.reply("Please submit a valid link.")
    except KeyError:
        if re.search(r"v\.redd\.it\/", url):
            ytdl.download([url])
            bot.say("https://actionsack.com/tmp/{}.{}".format(id, ext))
        else:
            bot.reply(
                "This video has no duration (livestream?) and cannot be downloaded.")
