import discord
from discord.ext import commands
import json

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot online as {bot.user}")
    await bot.tree.sync()

@bot.tree.command(name="products", description="View all Nexus Mart products")
async def products(interaction: discord.Interaction):
    with open("products.json") as f:
        data = json.load(f)

    embed = discord.Embed(
        title="🛒 Nexus Mart Products",
        description="Use tickets to order",
        color=discord.Color.blue()
    )

    for product, plans in data.items():
        text = ""
        for plan, price in plans.items():
            text += f"**{plan}** → {price}\n"
        embed.add_field(name=product, value=text, inline=False)

    await interaction.response.send_message(embed=embed)

bot.run("MTQ1MDU0OTAwMDE2MzAzNzE4NA.GxnHtF.cSVBRzmi6Jh83gnxK1swZ09aRsBPjeNTXVyV-A")
