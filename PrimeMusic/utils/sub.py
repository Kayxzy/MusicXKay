from pyrogram.errors import ChatAdminRequired, ChatWriteForbidden, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


from PrimeMusic import app


BANNED_USERS = set(int(x) for x in os.getenv("BANNED_USERS", "").split())
UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL")


def kay(_, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    rpk = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    if chat_id in BANNED_USERS:
        await app.send_message(
            chat_id,
            text=f"**❌ Anda telah di ban\nUbtuk menggunakan bot anda harus join di [Group](https://t.me/{UPDATES_CHANNEL})**",
            reply_to_message_id=message.message_id,
        )
        return
    ## Doing Force Sub 🤣
    update_channel = UPDATES_CHANNEL
    if update_channel:
        try:
            user = await app.get_chat_member(update_channel, user_id)
            if user.status == "kicked":
                await app.send_message(
                    chat_id,
                    text=f"**❌ Anda telah di ban\nUbtuk menggunakan bot anda harus join di [Group](https://t.me/{UPDATES_CHANNEL})**",
                    parse_mode="markdown",
                    disable_web_page_preview=True,
                )
                return
        except UserNotParticipant:
            await app.send_message(
                chat_id,
                text=f"""
**Halo {rpk} Untuk menghindari penggunaan yang berlebihan bot ini di khususkan untuk yang sudah join di group kami!**
""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "💬 Join Group Support 💬",
                                url=f"https://t.me/{update_channel}",
                            )
                        ]
                    ]
                ),
                parse_mode="markdown",
            )
            return
