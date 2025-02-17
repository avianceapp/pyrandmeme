"""
dpyrandmeme init file:

This is where the code is stored for the meme and discord-embed logic.
"""

import aiohttp
import discord
import random


async def pyrandmeme():
    lists_for_memes = ['https://www.reddit.com/r/GoCommitDie/rising.json?sort=rising',
                       'https://www.reddit.com/r/okbuddyretard/top.json?sort=top', 
                       'https://www.reddit.com/r/memes/rising.json?sort=rising', 
                       'https://www.reddit.com/r/meme/rising.json?sort=rising', 
                       'https://www.reddit.com/r/dank_meme/rising.json?sort=rising', 
                       'https://www.reddit.com/r/AdviceAnimals/rising.json?sort=rising',
                       'https://www.reddit.com/r/deepfriedmemes/rising.json?sort=rising',
                       'https://www.reddit.com/r/dankchristianmemes/rising.json?sort=rising',
                       'https://www.reddit.com/r/terriblefacebookmemes/rising.json?sort=rising',
                       'https://www.reddit.com/r/prequelmemes/rising.json?sort=rising',
                       'https://www.reddit.com//r/garlicbreadmemes/rising.json?sort=rising',
                       'https://www.reddit.com/r/offensivememes/rising.json?sort=rising',
                       'https://www.reddit.com/r/arabfunny/rising.json?sort=rising',
                       'https://www.reddit.com/r/darkmemes/rising.json?sort=rising',
                       'https://www.reddit.com/r/antimeme/rising.json?sort=rising',
                       'https://www.reddit.com/r/madlads/rising.json?sort=rising',
                       'https://www.reddit.com/r/funny/rising.json?sort=rising',]
    

    async with aiohttp.ClientSession() as cs:
        async with cs.get(lists_for_memes[random.randint(0, 16)]) as r:
            res = await r.json()
            var=res['data']['children'][random.randint(0, 16)]['data']
            pymeme = discord.Embed(url="https://www.reddit.com" + var['permalink'], title="**" + var['title'] + "**", color=0xe91e63)
            pymeme.set_image(url=var['url'])
            pymeme.set_footer(text='Post made by reddit user u/' + var['author'] + ' and posted in subreddit r/' + var['subreddit'] + '.')
            return pymeme
        await pyrandmeme()
