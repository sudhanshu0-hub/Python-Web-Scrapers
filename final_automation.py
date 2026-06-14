import os
import requests
from bs4 import BeautifulSoup

# System (Environment) se tokens aur IDs uthana
BOT_TOKEN = os.environ.get("FINAL_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def send_telegram_message(message):
    if not BOT_TOKEN or not CHAT_ID:
        print("❌ Error: FINAL_BOT_TOKEN ya TELEGRAM_CHAT_ID nahi mila! Pehle export kijiye.")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("✅ Success! Data Telegram par bhej diya gaya hai.")
        else:
            print(f"❌ Telegram Error: {response.text}")
    except Exception as e:
        print(f"❌ Message bhejne mein galti hui: {e}")

def start_automation():
    url = "http://quotes.toscrape.com/"
    print("🔄 Website se data nikal raha hu...")
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            quotes = soup.find_all('span', class_='text')
            authors = soup.find_all('small', class_='author')
            
            # Message ka header block
            text_message = "*🚀 Sudhanshu ka Advanced Scraper Bot Active Hai!* 🔥\n\n"
            
            # 5 quotes aur authors ko ek sunder message format mein jodna
            for i in range(min(5, len(quotes))):
                text_message += f"{i+1}. \"{quotes[i].text}\"\n✍️ _By {authors[i].text}_\n\n"
            
            # Telegram par final data bhejha
            send_telegram_message(text_message)
        else:
            print("❌ Website se data nahi nikala ja saka!")
    except Exception as e:
        print(f"❌ Scraping mein galti hui: {e}")

if __name__ == "__main__":
    start_automation()
