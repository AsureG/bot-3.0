#imports
import hikari
import lightbulb
import os
import json

bot = lightbulb.BotApp(
    TOKEN = os.environ.get("TOKEN")
    os.chdir(r'D:\Works\Codes\Bot 3.0 (hikari)\files'),
    default_enabled_guilds=(650256982200156172, 1004341322699780116),
    prefix=".",
    status="DND",
)

#events
@bot.listen(hikari.StartedEvent)
async def on_ready(event):
    print('Asurey 2.0 ready to go!')

#commands
@bot.command
@lightbulb.command("ping", "PONG")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond(f"Pong! \n`{round(bot.heartbeat_latency*1000)}ms latency`")

@bot.command
@lightbulb.command("hi", "Returns with a Hello")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond("Hello There")
    
@bot.command
@lightbulb.command("say", "Says the text")
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def say(self, ctx, *, text):
    message = ctx.message
    await message.delete()
    await ctx.send(f"{text}")

bot.run()