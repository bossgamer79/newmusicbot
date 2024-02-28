import re

from pyrogram import *
from pyrogram.types import *

from ... import *
from ... import __version__
from ...modules.helpers.buttons import *
from ...modules.helpers.inline import *
from ...modules.helpers.wrapper import *


@app.on_message(cdx(["help"]))
@sudo_users_only
async def inline_help_menu(client, message):
    image = None
    try:
        if image:
            bot_results = await app.get_inline_bot_results(
                f"@{bot.me.username}", "help_menu_logo"
            )
        else:
            bot_results = await app.get_inline_bot_results(
                f"@{bot.me.username}", "help_menu_text"
            )
        await app.send_inline_bot_result(
            chat_id=message.chat.id,
            query_id=bot_results.query_id,
            result_id=bot_results.results[0].id,
        )
    except Exception:
        bot_results = await app.get_inline_bot_results(
            f"@{bot.me.username}", "help_menu_text"
        )
        await app.send_inline_bot_result(
            chat_id=message.chat.id,
            query_id=bot_results.query_id,
            result_id=bot_results.results[0].id,
        )
    except Exception as e:
        print(e)
        return

    try:
        await message.delete()
    except:
        pass
      


@bot.on_callback_query(filters.regex(r"help_(.*?)"))
@cb_wrapper
async def help_button(client, query):
    plug_match = re.match(r"help_plugin\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)
    top_text = f"""
**🥀 𝙒𝙚𝙡𝙘𝙤𝙢𝙚 𝙏𝙤 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪 𝙊𝙛
𝙑𝘾 𝙐𝙨𝙚𝙧𝙗𝙤𝙩 » {__𝙫𝙚𝙧𝙨𝙞𝙤𝙣__} ✨...

Click On Below 🌺 Buttons To
Get Userbot Commands.

🌷Powered By : [⏤‌❥‌ 🖤𖣔ꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋ¤‌๋‌ࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧ𖣔ꠋꠋ𑲭𑲭𑲭🦋⃟≛⃝🖤҉𓆩⍣⃟𝐍𝐄𝐖 𝐉𝐀𝐘𝟕𝟗⍣⃟❤︎𓆪‌⍣⃟𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭𑲭](https://Telegram.me/NEWJAY79).**
"""
    
    if plug_match:
        plugin = plug_match.group(1)
        text = (
            "**🥀 Welcome To Help Menu Of:\n♨️ Plugin :** {}\n".format(
                plugs[plugin].__NAME__
            )
            + plugs[plugin].__MENU__
        )
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="↪️ Back", callback_data="help_back"
                    )
                ],
            ]
        )

        await bot.edit_inline_text(
            query.inline_message_id,
            text=text,
            reply_markup=key,
            disable_web_page_preview=True
        )
    elif prev_match:
        curr_page = int(prev_match.group(1))
        await bot.edit_inline_text(
            query.inline_message_id,
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_plugins(curr_page - 1, plugs, "help")
            ),
            disable_web_page_preview=True,
        )

    elif next_match:
        next_page = int(next_match.group(1))
        await bot.edit_inline_text(
            query.inline_message_id,
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_plugins(next_page + 1, plugs, "help")
            ),
            disable_web_page_preview=True,
        )

    elif back_match:
        await bot.edit_inline_text(
            query.inline_message_id,
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_plugins(0, plugs, "help")
            ),
            disable_web_page_preview=True,
        )

  