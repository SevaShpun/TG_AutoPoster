from configparser import NoSectionError

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from .. import AutoPoster
from ..utils import messages, tools


@AutoPoster.on_callback_query()
def callback(bot: AutoPoster, callback_query: CallbackQuery):
    if tools.admin_check(bot, callback_query):
        data = callback_query.data.split()
        if data[0] == "delete":
            bot.reload_config()
            try:
                section = {
                    **dict(last_id=0, last_story_id=0, pinned_id=0),
                    **bot.config["domains"].pop(data[1]),
                }
            except NoSectionError:
                info = "Источник {} не был найден. Возможно он был уже удален.".format(
                    data[1]
                )
            else:
                info = messages.SECTION_DELETED.format(data[1], **section)
            bot.save_config()
            callback_query.edit_message_text(info)
            return

        elif data[0] == "switch":
            bot.reload_config()
            global_ = bot.config.get("settings", {}).get(
                data[2],
                True
                if data[2] in ("disable_web_page_preview", "sign_posts")
                else False,
            )
            if data[1] == "global":
                bot.config["settings"][data[2]] = not global_
            else:
                local = bot.config["domains"][data[1]].get(data[2], global_)
                if not local == global_:
                    if data[2] in bot.config["domains"][data[1]].keys():
                        bot.config["domains"][data[1]].pop(data[2])
                else:
                    bot.config["domains"][data[1]][data[2]] = not local
            bot.save_config()
            info, reply_markup = tools.generate_setting_info(bot, data[1])
            callback_query.edit_message_text(
                info, reply_markup=reply_markup, disable_web_page_preview=True
            )
            return

        elif data[0] == "show":
            bot.reload_config()
            if data[2] == "send_reposts":
                info = "**Настройка отправки репостов:**\n\n"
                button_list = [
                    InlineKeyboardButton(
                        "Отключить", callback_data="reposts {} 0".format(data[1])
                    ),
                    InlineKeyboardButton(
                        "Включить", callback_data="reposts {} 1".format(data[1])
                    ),
                ]
                footer_buttons = [
                    InlineKeyboardButton(
                        "Только посты",
                        callback_data="reposts {} post_only".format(data[1]),
                    )
                ]
                button_list = tools.build_menu(
                    button_list, n_cols=2, footer_buttons=footer_buttons
                )

                option = bot.config["settings"]["send_reposts"]

                if data[1] != "global":
                    button_list.append(
                        [
                            InlineKeyboardButton(
                                "Использовать глобальное значение",
                                callback_data="reposts {} reset".format(data[1]),
                            )
                        ]
                    )

                if data[1] != "global":
                    if "send_reposts" in bot.config["domains"][data[1]].keys():
                        option = bot.config["domains"][data[1]].get("send_reposts")
                    else:
                        info = messages.SOURCE_USE_GLOBAL_SETTINGS

                if option == "post_only":
                    info += "Отправка только постов" + messages.PARTIAL_REPOSTS
                elif not option:
                    info += "Отправка репостов отключена"
                elif option:
                    info += "Отправка репостов включена"

                reply_markup = InlineKeyboardMarkup(button_list)
                callback_query.edit_message_text(info, reply_markup=reply_markup)
                return

        elif data[0] == "reposts":
            value = bool(int(data[2])) if data[2].isdigit() else data[2]
            if data[1] == "global":
                bot.config["settings"]["send_reposts"] = value
            else:
                if (
                    data[2] == "reset"
                    or bot.config["settings"]["send_reposts"] == value
                ):
                    if "send_reposts" in bot.config["domains"][data[1]].keys():
                        bot.config["domains"][data[1]].pop("send_reposts")
                else:
                    bot.config["domains"][data[1]]["send_reposts"] = value

            bot.save_config()

        info, reply_markup = tools.generate_setting_info(bot, data[1])
        callback_query.edit_message_text(
            info, reply_markup=reply_markup, disable_web_page_preview=True
        )
