import requests
from bs4 import BeautifulSoup
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Scrape.do se mila hua aapka token yahan set ho gaya hai
import os
PROXY_TOKEN = os.environ.get("SCRAPE_DO_TOKEN")

# Jis product ko track karna hai uski details
PRODUCT_URL = "https://www.amazon.in/dp/B0CHX1W1XY"
TARGET_PRICE = 70000

# Scrape.do ka API URL jo Amazon ke block ko bypass karega
API_URL = f"https://api.scrape.do?token={PROXY_TOKEN}&url={PRODUCT_URL}"

def check_price():
    try:
        print("Proxy ke zariye Amazon se data nikal raha hu...")
        response = requests.get(API_URL, timeout=30)
        
        if response.status_code != 200:
            print(f"API Error Code: {response.status_code}. Token ya connection check karein.")
            return

        soup = BeautifulSoup(response.content, "lxml")

        # Amazon ke dynamic layouts ke liye alag-alag selectors check karna
        title_el = soup.find(id="productTitle") or soup.find("span", {"id": "productTitle"})
        if not title_el:
            print("Product Title nahi mila. Amazon layout badal raha hai.")
            return
            
        title = title_el.get_text().strip()
        
        price_element = soup.find("span", class_="a-price-whole") or soup.find("span", {"class": "a-offscreen"})
        if not price_element:
            print("Price nahi mil payi.")
            return

        price_text = price_element.get_text().replace(",", "").replace(".", "").replace("₹", "").strip()
        current_price = int(price_text)

        print(f"Product: {title[:50]}...")
        print(f"Current Price: ₹{current_price}")

        if current_price < TARGET_PRICE:
            print("Price kam ho gaya! Email bhej raha hu...")
            send_mail(title, current_price)
        else:
            print("Price abhi target se zyada hai.")

    except Exception as e:
        print(f"Error aaya: {e}")

def send_mail(product_title, price):
    sender_email = "Sudhanshumaurya6633@gmail.com"
PROXY_TOKEN = os.environ.get("SCRAPE_DO_TOKEN")
    receiver_email = "Sudhanshumaurya6633@gmail.com"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = f"PRICE DROP ALERT! {product_title[:30]}..."

    body = f"Good News! Price drop ho gaya hai.\n\nProduct: {product_title}\nNew Price: ₹{price}\nLink: {PRODUCT_URL}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print("Email kamyabi se bhej diya gaya!")
        server.quit()
    except Exception as e:
        print(f"Email bhejne mein dikkat aayi: {e}")

if __name__ == "__main__":
    while True:
        check_price()
        print("Agli check 1 ghante baad hogi...")
        time.sleep(3600)
