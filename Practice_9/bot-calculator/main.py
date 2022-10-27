import re
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
MY_TOKEN = "YOUR TOKEN"


def calc(expresiion: str):
    cleared_expresion = clearExpresiion(expresiion)
    return eval(cleared_expresion)


def clearExpresiion(input_str: str):
    return re.sub(r'[^\d+=*%^/\(\)\-]', "", input_str)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_html(
        "Добро пожаловать в калькулятор, введите выражение для расчета, например: 1 + 2",
        reply_markup=ForceReply(selective=True),
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = f"Результат выражения: {calc(update.message.text)}"
    await update.message.reply_text(message)


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(MY_TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
