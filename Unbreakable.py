# I honestly don't give a shit if you delete this, but I would appreciate if you don't

#                     AUTHOR : ts1

# ---------------   TECHNICAL SUPPORT   --------------- #
#  https://discordpy.readthedocs.io/en/stable/faq.html  #
#                    discord : ts1                      #
#               mail : ts1.dev@icloud.com               #
# ----------------------------------------------------- #

import discord
from discord import app_commands
from discord.ext import commands

# Initializing all intents you need
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

# Initializing bot w intents, change prefix
bot = commands.Bot(command_prefix="/", intents=intents)

# Commands tree
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Some logs, I will add more in future (if I still care about this)
@bot.event
async def on_ready():
    print("Bot info : ")
    print("Username : ", bot.user.name)
    print("User ID : ", bot.user.id)
    
    try:
        # Synchronizing all commands with a specified guilds (server)
        synced = await bot.tree.sync(guild=discord.Object(id=1106370076321529936))
        print(f"Synchronized {len(synced)} commands")
    
    except Exception as e:
        print(e)

# first slash commands
@bot.tree.command(guild=discord.Object(id=1106370076321529936), name="commandtest", description="My First Command")
async def test_slash(interaction: discord.Interaction):
    # Création de l'embed avec la couleur noire définie par code hexadécimal
    first_embed = discord.Embed(
        title="Title",
        description="Description",
        color=discord.Color.from_rgb(0, 0, 0)  # Color
    )
    
    # Envoi de l'embed en réponse à l'interaction
    await interaction.response.send_message(embed=first_embed)

# Lancement du bot avec le nouveau token
bot.run("Your TOKEN")

