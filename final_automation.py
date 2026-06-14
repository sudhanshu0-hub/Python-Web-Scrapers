import requests
from bs4 import BeautifulSoup

BOT_TOKEN = "8948830066:AAHZjyQjwE63oBjJ8OZi96-feW8KloJEz5Q"
CHAT_ID = "845580463"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("✅ Success! Data Telegram par bhej diya gaya hai.")
    else:
        print(f"❌ Telegram Error: {response.text}")

def start_automation():
    url = "http://quotes.toscrape.com/"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('span', class_='text')
        authors = soup.find_all('small', class_='author')
        
        # Message ka header block
        text_message = "*🔥 Sudhanshu ka Advanced Scraper Bot Active Hai! 🔥*\n\n"
        
        # 5 quotes aur authors ko ek sunder message format mein jodna
        for i in range(5):
            text_message += f"{i+1}. \"{quotes[i].text}\"\n✍️ _- By {authors[i].text}_\n\n"
        
        # Telegram par final data bhejna
        send_telegram_message(text_message)
    else:
        print("Website se data nahi nikala ja saka!")

if __name__ == "__main__":
    start_automation()
