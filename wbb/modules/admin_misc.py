import os

from pyrogram import filters

from wbb import app
from wbb.core.decorators.permissions import adminsOnly

__MODULE__ = "Admin Miscs"
__HELP__ = """
/set_chat_title - Change The Name Of A Group/Channel.
/set_chat_photo - Change The PFP Of A Group/Channel.
/set_user_title - Change The Administrator Title Of An Admin.
"""


@app.on_message(filters.command("sesakjfhjas") & ~filters.private)
@adminsOnly("can_change_info")
async def set_chat_title(_, message):
    if len(message.command) < 2:
        return await message.reply_text("**Usage:**\n/set_chat_title NEW NAME")
    old_title = message.chat.title
    new_title = message.text.split(None, 1)[1]
    await message.chat.set_title(new_title)
    await message.reply_text(
        f"Successfully Changed Group Title From {old_title} To {new_title}"
    )


@app.on_message(filters.command("set_sajkgfjag") & ~filters.private)
@adminsOnly("can_change_info")
async def set_user_title(_, message):
    chat_id = message.chat.id
    from_user = message.reply_to_message.from_user
    if len(message.command) < 2:
        return await message.reply_text(
            "**Usage:**\n/set_user_title NEW ADMINISTRATOR TITLE"
        )
    title = message.text.split(None, 1)[1]
    await app.set_administrator_title(chat_id, from_user.id, title)
    await message.reply_text(
        f"Successfully Changed {from_user.mention}'s Admin Title To {title}"
    )


@app.on_message(filters.command("setasjhgfasj") & ~filters.private)
@adminsOnly("can_change_info")
async def set_chat_photo(_, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "Reply to a photo to set it as chat_photo"
        )
    if (
        not message.reply_to_message.photo
        and not message.reply_to_message.document
    ):
        return await message.reply_text(
            "Reply to a photo to set it as chat_photo"
        )
    photo = await message.reply_to_message.download()
    await message.chat.set_photo(photo)
    await message.reply_text("Successfully Changed Group Photo")
    os.remove(photo)
