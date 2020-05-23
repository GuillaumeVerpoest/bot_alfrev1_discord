# import discord
import discord
from discord.ext import commands


# jeton de alfredv1
jeton = "NzEzMDA0NjQyNDM0NTQ3NzE1.XsZ03w.pAtjESUygBx1oNVYgbtQq7AnlxE"
bot = commands.Bot(command_prefix=('!'))

# eveil de alfredv1
@bot.event
async def on_ready():
    print("bot pret")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("Creation en cour"))
    #await sa_montre()


@bot.command()
async def chrono(ctx):
    await ctx.send("Le chrono n'est pas fait")


@bot.command()
async def planning(ctx, categorie):
    if(categorie == "stop"):
        await ctx.send("lance la function stop")
    elif categorie == "Code":
        await ctx.send("lance le timer dans le bonne colonne ")
    else:
        await ctx.send("error !planning")

@planning.error
async def on_command_error(ctx, error):
    # detecter cette erreur
    if isinstance(error, commands.MissingRequiredArgument):
        # envoyer un message
        await ctx.send("La commande est : !planning *categorie*")
    #afficher un message error








print("Lancement du bot...")
bot.run(jeton)