# import discord
import discord
from discord.ext import commands
from main import *

#jeton de alfredv1
jeton = "NzEzMDA0NjQyNDM0NTQ3NzE1.XszVqA.lw90CCsKg0BZ37wBuf6M2ecbNzo"
bot = commands.Bot(command_prefix=('!'))

#evail de alfredv1
@bot.event
async def on_ready():
    print("Bot prêt")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("En court de creation"))

@bot.command()
async def planning(ctx, categorie):
    colomns_today = Planning_Alfredv1().get_day()
    message_alfred = Planning_Alfredv1().add_activity(colomns_today, categorie)
    await ctx.send(message_alfred)

@bot.command()
async def stop(ctx, categorie):
    colomns_today = Planning_Alfredv1().get_day()
    message_alfred = Planning_Alfredv1().stop_activity(colomns_today, categorie)
    await ctx.send(message_alfred)

@planning.error
async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("La command est : !planning *activity*")

print("Lancement du bot...")
bot.run(jeton)