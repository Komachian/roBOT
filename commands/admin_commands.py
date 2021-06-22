"""
Module containing functions for all the admin commands.
"""

from commands.scripts import loader

db = loader.db_loaded()

async def clean(message):
    await message.channel.purge(limit=100)


async def configure(message):
    await db.server_config(message.guild.id, message)


async def deconfigure(message):
    await db.server_deconfig(message.guild.id, message)


async def leave(message):
    await db.leave_server(message.guild.id, message)


async def moderation(message):
    await db.moderation_service(message.guild.id, message)


async def kick(message):
    if message.mentions.__len__() > 0:
        for user in message.mentions:
            user = await message.guild.query_members(user_ids=[user.id])
        user = user[0]
        await user.kick(reason="Kicked by roBOT!")


async def mute(message):
    if message.mentions.__len__() > 0:
        for user in message.mentions:
            user = await message.guild.query_members(user_ids=[user.id])
        user = user[0]

        try:
            await user.edit(mute=True)
        except Exception:
            await message.channel.send("User's not connected to voice!")


async def unmute(message):
    if message.mentions.__len__() > 0:
        for user in message.mentions:
            user = await message.guild.query_members(user_ids=[user.id])
        user = user[0]
        try:
            await user.edit(mute=False)
        except Exception:
            await message.channel.send("User's not connected to voice!")


async def configconfess(message):
    await db.confess_config(message.guild.id, message)


async def deconfigconfess(message):
    await db.confess_deconfig(message.guild.id, message)
