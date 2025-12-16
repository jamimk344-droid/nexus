import discord
from discord.ext import commands
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise ValueError("❌ DISCORD_TOKEN not found in environment variables")

# Bot intents
intents = discord.Intents.default()

# Create bot
bot = commands.Bot(command_prefix="!", intents=intents)

# -------------------- EVENTS --------------------

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"✅ Nexus Mart Bot is online as {bot.user}")

# -------------------- SLASH COMMANDS --------------------

@bot.tree.command(name="products", description="View all available Nexus Mart products")
async def products(interaction: discord.Interaction):
    try:
        with open("products.json", "r", encoding="utf-8") as f:
            products = json.load(f)
    except FileNotFoundError:
        await interaction.response.send_message(
            "❌ products.json file not found.",
            ephemeral=True
        )
        return

    embed = discord.Embed(
        title="🛒 Nexus Mart Products",
        description="Open a ticket to place an order",
        color=discord.Color.blue()
    )

    for product_name, plans in products.items():
        value = ""
        for plan, price in plans.items():
            value += f"**{plan}** → {price}\n"
        embed.add_field(
            name=product_name,
            value=value,
            inline=False
        )

    embed.set_footer(text="Nexus Mart • Trusted Digital Store")

    await interaction.response.send_message(embed=embed)

# -------------------- RUN BOT --------------------

bot.run(TOKEN)
