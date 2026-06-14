import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging taaki agar koi galti ho toh pata chale
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

# Aapka unique token yahan set kar diya hai
TOKEN = "8972490399:AAHXoZoJe1QedSavVx4vF2gU80D6aLyyVx0"

# 1. /start command ka jawab
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_name = update.effective_user.first_name
    welcome_msg = (
        f"👋 Namaste {user_name} aap!\n\n"
        "🤖 Main aapka personal E-commerce Scraper Bot hu.\n"
        "💼 Main aapke clients ke liye data nikal kar yahan bhej sakta hu.\n\n"
        "👉 Laptops ka taaza data dekhne ke liye type karein: /getlaptops"
    )
    await update.message.reply_text(welcome_msg)

# 2. /getlaptops command ka jawab (CSV file se data padhkar bhejna)
async def get_laptops(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🔄 File se data nikal raha hu, ek second rukiye...")
    
    try:
        # Humari banayi hui laptops_data.csv file ko kholna
        with open("laptops_data.csv", "r", encoding="utf-8") as file:
            lines = file.readlines()[1:6] # Pehle 5 laptops ka data nikalna
            
        response_text = "💻 **Top 5 Laptops Data:**\n\n"
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) >= 2:
                response_text += f"🔹 **Product:** {parts[0]}\n💰 **Price:** {parts[1]}\n\n"
                
        await update.message.reply_text(response_text, parse_mode="Markdown")
    except FileNotFoundError:
        await update.message.reply_text("❌ Error: 'laptops_data.csv' file nahi mili. Pehle scraper chalaiye!")

# Main function jo bot ko chalu rakhega
def main():
    print("🚀 Telegram Bot start ho raha hai... Apne Telegram app par jaakar check kijiye!")
    app = Application.builder().token(TOKEN).build()

    # Commands ko link karna
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("getlaptops", get_laptops))

    # Bot ko chalu rakhna (Polling)
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
