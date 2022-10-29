from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, ConversationHandler
from enum import Enum
from datetime import datetime
import database
import peoples
TOKEN = "5438425757:AAEfxTM9GX8rYti_57TyIVjq3Pd8vv7uCGs"
storage = None
LASTNAME, NAME, THIRDNAME, BIRTHDATE, PHONE = range(5)
SEARCH, ADD, UPDATE, DELETE, LIST = range(5)
OLD_PHONE, NEW_PHONE = range(2)
insertData = dict()
updateData = dict()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text("Welcome to telephone note!")


async def list_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """List all peoples in the note!"""
    _peoples = peoples.findAll()
    print(" | ".join(map(lambda p: peoples.people_to_string(p), _peoples)))
    if len(_peoples) == 0:
        await update.message.reply_text("Note doesn't have any note! Try add.")
        return
    await update.message.reply_text("\n".join(map(lambda p: peoples.people_to_string(p), _peoples)))


async def add_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Command for insert new people data into the note"""
    await update.message.reply_text("You are in add mode! Please, enter lastname.")
    return LASTNAME


async def update_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Update people phone"""
    await update.message.reply_text("For update, please enter people's phone!")
    return OLD_PHONE


async def delete_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Command for delete people from the note"""
    await update.message.reply_text("Type user id for delete!")
    return DELETE


async def find_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Command for find people by phone"""
    await update.message.reply_text("Please enter phone for searching!")
    return SEARCH


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Cancel conversation"""
    global insertData
    global updateData
    insertData = dict()
    updateData = dict()
    await update.message.reply_text("See you in the next time!")
    return ConversationHandler.END


async def lastname_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global insertData
    insertData["lastname"] = update.message.text
    await update.message.reply_text("Next, enter firstname, please")
    return NAME


async def name_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    insertData["name"] = update.message.text
    await update.message.reply_text("Next, enter thirdname, please")
    return THIRDNAME


async def thirdname_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    insertData["thirdname"] = update.message.text
    await update.message.reply_text("Next, enter bithdate (like: 2002-11-20), please")
    return BIRTHDATE


async def birthdate_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    f = "%Y-%m-%d"  # 2002-11-10
    insertData["birthdate"] = datetime.strptime(update.message.text, f)
    await update.message.reply_text("Next, enter phone, please")
    return PHONE


async def phone_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    insertData["phone"] = update.message.text
    peoples.insert(insertData)
    await update.message.reply_text("Successfuly added!")
    return ConversationHandler.END


async def update_old_phone_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    updateData["old_phone"] = update.message.text
    people = peoples.find(updateData["old_phone"])
    await update.message.reply_text(f"Find: {people}")
    await update.message.reply_text("Enter new phone!")
    return NEW_PHONE


async def update_new_phone_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    new_phone = update.message.text
    peoples.updatePhone(updateData["old_phone"], new_phone)
    await update.message.reply_text("Phone updated!")
    return ConversationHandler.END


async def delete_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    id = update.message.text
    peoples.delete(id)
    await update.message.reply_text("People deleted!")
    return ConversationHandler.END


async def find_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    phone = update.message.text
    people = peoples.find(phone)
    if len(people) == 0:
        await update.message.reply_text("People with this phone not found!")
        return
    p_string = '\n'.join(map(lambda p: peoples.people_to_string(p), people))
    await update.message.reply_text(f"Find people: {p_string}")
    return ConversationHandler.END


def main() -> None:
    global storage
    storage = database.init()
    """Start the bot."""

    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()
    cancel_conv_handler = CommandHandler("cancel", cancel)
    # Add conversation handler
    add_conv_handler = ConversationHandler(
        entry_points=[CommandHandler("add", add_command)],
        states={
            LASTNAME: [MessageHandler(filters.TEXT, lastname_message)],
            NAME: [MessageHandler(filters.TEXT, name_message)],
            THIRDNAME: [MessageHandler(filters.TEXT, thirdname_message)],
            BIRTHDATE: [MessageHandler(filters.TEXT, birthdate_message)],
            PHONE: [MessageHandler(filters.TEXT, phone_message)],
        },
        fallbacks=[cancel_conv_handler]
    )
    # Update conversation handeler
    update_conv_handler = ConversationHandler(
        entry_points=[CommandHandler("update", update_command)],
        states={
            OLD_PHONE: [MessageHandler(filters.TEXT, update_old_phone_message)],
            NEW_PHONE: [MessageHandler(filters.TEXT, update_new_phone_message)],
        },
        fallbacks=[cancel_conv_handler]
    )
    # Delete conversation handler
    delete_conv_hander = ConversationHandler(
        entry_points=[CommandHandler("delete", delete_command)],
        states={
            DELETE: [MessageHandler(filters.TEXT, delete_message)],
        },
        fallbacks=[cancel_conv_handler]
    )
    # Find conversation handler
    find_conv_handler = ConversationHandler(
        entry_points=[CommandHandler("find", find_command)],
        states={
            SEARCH: [MessageHandler(filters.TEXT, find_message)]
        },
        fallbacks=[cancel_conv_handler]
    )
    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("list", list_command))
    application.add_handler(add_conv_handler)
    application.add_handler(update_conv_handler)
    application.add_handler(delete_conv_hander)
    application.add_handler(find_conv_handler)

    # on non command i.e message - echo the message on Telegram
    application.run_polling()


if __name__ == "__main__":
    main()
