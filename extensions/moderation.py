from disnake.ext import commands
from disnake import Color, Embed, CommandInteraction, Member, Forbidden
from disnake_plugins import plugin

plugin = plugin.Plugin()

@plugin.slash_command(name="ban", description="Ban member from the server")
@commands.bot_has_permissions(ban_members=True)
@commands.has_permissions(ban_members=True)
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
async def ban(inter:CommandInteraction, member:Member, clear_message_history:bool=False, reason:str="No reason provided"):
    if clear_message_history:
        await member.ban(clean_history_duration=member.joined_at.timestamp, reason=reason)
    else:
        await member.ban(reason=reason)
    
    await inter.response.send_message(embed=Embed(title="Member banned", color=Color.green()))

# @ban.error
# async def on_ban_error(inter, error):
#     if isinstance(error, Forbidden):
#         await inter.response.send_message(embed=Embed(title="Bot missing permission", description="This command requires the `ban members` permission", color=Color.red()))
#     elif isinstance(error, commands.MissingPermissions):
#         await inter.response.send_message(embed=Embed(title="Missing permission", description="You do not have permisson to do this", color=Color.red()))
#     elif isinstance(error, commands.CommandOnCooldown):
#         await inter.response.send_message(embed=Embed(title="Command on cooldown", description=f"Try again in {round(error.retry_after, 2)} seconds", color=Color.red()))
#     else:
#         await inter.response.send_message(embed=Embed(title="Unknown error occured", description=f"{error} occured, ping KarsonTheFoxx", color=Color.red()))

@plugin.slash_command(name="kick")
@commands.bot_has_permissions(kick_members=True)
@commands.has_permissions(kick_members=True)
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
async def kick(inter:CommandInteraction, member:Member, reason:str="No reason provided"):
    await member.kick(reason=reason)
    await inter.response.send_message(embed=Embed(title="Member kicked", color=Color.green()))

# @kick.on_error
# async def on_kick_error(inter, error):
#     if isinstance(error, Forbidden):
#         await inter.response.send_message(embed=Embed(title="Bot missing permission", description="This command requires the `kick members` permission", color=Color.red()))
#     elif isinstance(error, commands.MissingPermissions):
#         await inter.response.send_message(embed=Embed(title="Missing permission", description="You do not have permisson to do this", color=Color.red()))
#     elif isinstance(error, commands.CommandOnCooldown):
#         await inter.response.send_message(embed=Embed(title="Command on cooldown", description=f"Try again in {round(error.retry_after, 2)} seconds", color=Color.red()))
#     else:
#         await inter.response.send_message(embed=Embed(title="Unknown error occured", description=f"{error} occured, ping KarsonTheFoxx", color=Color.red()))


@plugin.slash_command(name="purge", description="Purge X number of messages")
@commands.bot_has_permissions(manage_messages=True)
@commands.has_permissions(manage_messages=True)
@commands.cooldown(rate=2, per=60, type=commands.BucketType.user)
async def purge(inter:CommandInteraction, number_messages:int):
    await inter.channel.purge(limit=number_messages)
    await inter.response.send_message(embed=Embed(title="Purge complete", color=Color.green()))

# @purge.error
# async def on_purge_error(inter, error):
#     if isinstance(error, Forbidden):
#         await inter.response.send_message(embed=Embed(title="Bot missing permission", description="This command requires the `manage messages` permission", color=Color.red()))
#     elif isinstance(error, commands.MissingPermissions):
#         await inter.response.send_message(embed=Embed(title="Missing permission", description="You do not have permisson to do this", color=Color.red()))
#     elif isinstance(error, commands.CommandOnCooldown):
#         await inter.response.send_message(embed=Embed(title="Command on cooldown", description=f"Try again in {round(error.retry_after, 2)} seconds", color=Color.red()))
#     else:
#         await inter.response.send_message(embed=Embed(title="Unknown error occured", description=f"{error} occured, ping KarsonTheFoxx", color=Color.red()))

@plugin.slash_command(name="mute", description="s = second, m = minute, h = hour, d = day")
@commands.bot_has_permissions(mute_members=True)
@commands.has_permissions(mute_members=True)
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
async def mute(inter:CommandInteraction, member:Member, duration:str):
    if duration.lower().endswith("s"):
        await member.timeout(duration=int(duration[:-1]))
    elif duration.lower().endswith("m"):
        await member.timeout(duration=int(duration[:-1])*60)
    elif duration.lower().endswith("h"):
        await member.timeout(duration=int(duration[:-1])*3600)
    elif duration.lower().endswith("d"):
        await member.timeout(duration=int(duration[:-1])*86400)
    
    await inter.response.send_message(embed=Embed(title="Member timed out", description="To remove timeout, run this command again and set the time to 0", color=Color.green()))

# @mute.error
# async def on_mute_error(inter, error):
#     if isinstance(error, Forbidden):
#         await inter.response.send_message(embed=Embed(title="Bot missing permission", description="This command requires the `mute members` permission", color=Color.red()))
#     elif isinstance(error, commands.MissingPermissions):
#         await inter.response.send_message(embed=Embed(title="Missing permission", description="You do not have permisson to do this", color=Color.red()))
#     elif isinstance(error, commands.CommandOnCooldown):
#         await inter.response.send_message(embed=Embed(title="Command on cooldown", description=f"Try again in {round(error.retry_after, 2)} seconds", color=Color.red()))
#     else:
#         await inter.response.send_message(embed=Embed(title="Unknown error occured", description=f"{error} occured, ping KarsonTheFoxx", color=Color.red()))
        

setup, teardown = plugin.create_extension_handlers()