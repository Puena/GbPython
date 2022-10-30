import re
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import logging
MY_TOKEN = "YOUR TOKEN"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def clearExpresiion(input_str: str):
    return re.sub(r'[^\d+=*%^/\(\)\-]', "", input_str)


def calc(expresiion: str):
    cleared_expresion = clearExpresiion(expresiion)
    return eval(cleared_expresion)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    logger.info("Start")
    await update.message.reply_text(
        "Добро пожаловать в калькулятор, введите выражение для расчета, например: 1 + 2"
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("User input {}".format(update.message.text))
    result = calc(update.message.text)
    logger.info("Result is: {}".format(update.message.text))
    message = f"Результат выражения: {result}"
    await update.message.reply_text(message)


def main() -> None:
    """Start the bot."""
    logger.info("Bot started!")
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
