# import discord
import discord
from discord.ext import commands
from bot_planning_alfredv1 import get_hour_in_planning, Planning_Alfredv1


# jeton de alfredv1
jeton = "NzEzMDA0NjQyNDM0NTQ3NzE1.XsuMfQ.XyIN1DtA-GPoUJ550uFqQh3evhI"
bot = commands.Bot(command_prefix=('!'))
verif_categorie = ["Code","Anglais","Devolepement_Perso", "Libre"]

# eveil de alfredv1
@bot.event
async def on_ready():
    print("bot pret")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("En court de cration"))
    #await sa_montre()


@bot.command()
async def chrono(ctx):
    await ctx.send("Le chrono n'est pas fait")


@bot.command()
async def planning(ctx, categorie):
    day_planning = Planning_Alfredv1().get_planning_day()
    time = Planning_Alfredv1().add_planning(day_planning, categorie)
    if (categorie in verif_categorie):
        await ctx.send(time)

@bot.command()
async def stop(ctx, categorie):
    day_planning = Planning_Alfredv1().get_planning_day()
    time = Planning_Alfredv1().add_planning(day_planning, categorie)
    if (categorie in verif_categorie):
        Planning_Alfredv1().stop(day_planning, categorie, time)
        await ctx.send("J'arrete le chrono")

@planning.error
async def on_command_error(ctx, error):
    # detecter cette erreur
    if isinstance(error, commands.MissingRequiredArgument):
        # envoyer un message
        await ctx.send("La commande est : !planning *categorie*")
    #afficher un message error








print("Lancement du bot...")
bot.run(jeton)