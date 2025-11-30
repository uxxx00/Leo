import discord
from discord.ext import commands

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready! Logged in as {bot.user}")

@bot.tree.command(name="ping", description="Replies with Pong!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")

# Run the bot
if __name__ == "__main__":
    import os
    TOKEN = os.environ.get("DISCORD_TOKEN")  # Or paste your bot token here directly
    bot.run(TOKEN)
