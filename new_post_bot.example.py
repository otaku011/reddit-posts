import asyncio
import discord
import logging
import praw
import time
import traceback
from discord.ext import commands

bot = commands.Bot(command_prefix=';;')

logging.basicConfig(
    filename="output.log",
    filemode='a',
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
    level=logging.INFO
)
logging.getLogger().addHandler(logging.StreamHandler())

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="Discord bot (for /r/animepiracy)"
)

subreddit = "animepiracy"


async def check_for_posts():
    await bot.wait_until_ready()
    bot_started_at = time.time()
    logging.info(f"Logged into Discord as user: {bot.user.name}.")
    cache = []

    while True:
        try:
            for submission in reddit.subreddit(subreddit).new(limit=10):
                if submission.id in cache:
                    continue

                if submission.created_utc <= bot_started_at:
                    continue

                logging.info(f"{submission.title} was posted by /u/{submission.author.name}")

                embed = discord.Embed(
                    title="r/" + subreddit + " - " + submission.title,
                    url=submission.url,
                    description=submission.selftext[0:350],
                )

                embed.set_author(
                    name=f"/u/{submission.author.name}",
                    url=f"https://reddit.com/u/{submission.author.name}"
                )

                embed.set_thumbnail(url=submission.author.icon_img)

                if len(submission.selftext) > 350:
                    embed.description = embed.description + "..."

                channel = bot.get_channel(0000000000000000)
                await channel.send(embed=embed)
                cache.append(submission.id)

            await asyncio.sleep(3)

        except Exception as e:
            logging.error(e)
            traceback.print_exc()
            time.sleep(30)
            pass


bot.loop.create_task(check_for_posts())
bot.run("")
