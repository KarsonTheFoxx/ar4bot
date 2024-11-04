from disnake.ext import tasks
from disnake_plugins import plugin
from disnake import Embed, Color

from datetime import timedelta, datetime, timezone

plugin = plugin.Plugin()

@plugin.register_loop(wait_until_ready=True)
@tasks.loop(hours=168)
async def update_server_stats():
    guild = plugin.bot.get_guild(1300267963462582282)
    embed = Embed(title=f"{guild.name} stats", description=f"Some statistics about this guild\n-# Next update <t:{int((datetime.now(timezone.utc) + timedelta(days=7)).timestamp())}:R>\n-# Current date: <t:{int(datetime.now(timezone.utc).timestamp())}:d>", color=Color.random())

    embed.add_field(name="Total member count", value=guild.member_count, inline=True)
    embed.add_field(name="User member count", value=len([member for member in guild.members if member.bot == False]), inline=True)
    embed.add_field(name="Bot member count", value=len([member for member in guild.members if member.bot == True]), inline=True)
    
    await guild.get_channel(1302830133081804851).send(embed=embed)

setup, teardown = plugin.create_extension_handlers()

if __name__ == "__main__":
    print("Run main.py instead!")