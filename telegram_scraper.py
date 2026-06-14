import requests
from bs4 import BeautifulSoup

BOT_TOKEN = "8948830066:AAHZjyQjwE63oBjJ8OZi96-feW8KloJEz5Q"
CHAT_ID = "845580463"

def send_telegram_message(message):
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    try:
        response = requests.post(telegram_url, json=payload)
        if response.status_code == 200:
            print("Telegram par message safalta-purvak bhej diya gaya!")
        else:
            print(f"Telegram Error: {response.text}")
    except Exception as e:
        print(f"Connection Error: {e}")

def scrape_and_send():
    url = "http://quotes.toscrape.com/"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('span', class_='text')
        authors = soup.find_all('small', class_='author')
        
        text_to_send = "*🔥 Aapka Pehla Automation Bot Live Hai! 🔥*\n\n"
        for i in range(3):
            text_to_send += f"{i+1}. \"{quotes[i].text}\"\n_- By {authors[i].text}_\n\n"
        
        send_telegram_message(text_to_send)
    else:
        print("Website se data nahi nikala ja saka!")

if __name__ == "__main__":
    scrape_and_send()
