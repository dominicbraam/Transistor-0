import discord
from discord.ext import commands
from dotenv import load_dotenv
from dateutil.parser import parse as dtparse
from datetime import datetime
from datetime import date
from datetime import timedelta
from os import getenv
import cal_handler
load_dotenv()

def main():
    bot = commands.Bot(command_prefix='!')

    intents = discord.Intents.default()
    intents.members = True

    # time_format = '%d %B, %H:%M %p'

    @bot.command()
    async def hello(ctx):
        await ctx.reply('Hey there!')

    @bot.command()
    async def showcommands(ctx):
        await ctx.reply('Coming Soon')

    @bot.command()
    async def today(ctx):
        reply = create_summary(date.today())
        await ctx.reply(reply)

    @bot.command()
    async def tomorrow(ctx):
        reply = create_summary(date.today() + timedelta(days=1))
        await ctx.reply(reply)

    bot.run(getenv('TOKEN'))

def compile_classes(classes):
    time_format = '%H:%M'

    if not classes:
        classes_summary = "You have no classes!!!"
    else:
        classes_summary = ""
        for class_ in classes:
            # https://stackoverflow.com/questions/49889379/google-calendar-api-datetime-format-python
            event_time = datetime.strftime(dtparse(class_["start"]["dateTime"]), format=time_format)
            event_item = class_["summary"] + " - " + event_time
            classes_summary += event_item + "\n"

    compiled_classes = "-- CLASSES --\n" + classes_summary

    return compiled_classes

def create_summary(date):
    events = cal_handler.get_events(date)
    summary = compile_classes(events)
    return summary

if __name__ == "__main__":
    main()
