from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Функция /start с кнопкой "Запуск кликера"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user

    # URL вашего веб-приложения, например: F:\1.ЗАГРУЗКИ\BD\cliker\html.html
    web_app_url = "F:\1.ЗАГРУЗКИ\BD\cliker\html.html"

    keyboard = [
        [
            InlineKeyboardButton("Запуск кликера", web_app=web_app_url)
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"Привет, {user.first_name}! Добро пожаловать в кликер!",
        reply_markup=reply_markup
    )

# Остальные функции (если нужны)
async def click(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Клик зарегистрирован!")

async def upgrade_card(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Карточка улучшена!")

async def get_income(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Прибыль начислена!")

async def leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Топ игроков!")

# Создание экземпляра приложения
application = Application.builder().token("5458560576:AAHe_ZYyRlUa7FUn-E1t8MTW9ZhHLBaprz0").build()

# Добавление обработчиков команд и кнопок
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("click", click))
application.add_handler(CommandHandler("upgrade", upgrade_card))
application.add_handler(CommandHandler("income", get_income))
application.add_handler(CommandHandler("leaderboard", leaderboard))

# Запуск бота
application.run_polling()
