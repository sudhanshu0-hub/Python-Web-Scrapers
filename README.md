# 🚀 Professional Web Scraping & Business Automation Suite

Welcome to my portfolio! This repository contains a collection of high-performance, secure, and production-ready Python automation scripts designed to solve real-world business challenges. From automated market research to instant pricing trackers, these tools help businesses save hours of manual labor.

---

## 🛠️ Key Featured Projects

### 1. 📊 Automated Market Research Analyst (`analyze_market.py`)
This tool uses **Pandas** to ingest scraped e-commerce product listings and generate instant business intelligence reports. 
* **Key Features:** Automatic column mapping, price cleaning, and outlier detection.
* **Outputs:** Calculates average market price, identifies the most expensive/affordable products, and ranks the top 5 best deals.
* **Business Value:** Saves hours of manual spreadsheet analysis, allowing e-commerce sellers to price their products competitively.

### 2. 🛡️ Secure Amazon Price Tracker with Email Alerts (`amazon_tracker.py`)
A background monitoring script that tracks high-value products on Amazon and sends instant email notifications when prices drop below a user-defined threshold.
* **Key Features:** Employs **Scrape.do API** proxies to seamlessly bypass anti-bot detection; uses environment variables to secure sensitive credentials.
* **Outputs:** Automated email alert templates sent via SMTP on Google Mail.

### 3. 🤖 E-Commerce Scraper & Telegram Notification Bot (`telegram_bot.py`)
An interactive scraping workflow that extracts e-commerce data and instantly pushes structured message updates to a specified Telegram Chat or Channel.
* **Key Features:** Built on the `python-telegram-bot` framework and utilizes clean formatting for rich-text notifications.
* **Business Value:** Perfect for affiliate marketers or bargain-hunters who need real-time data delivered straight to their mobile devices.

---

## ⚙️ Professional Best Practices Implemented
* **Zero-Hardcoding Security:** All sensitive API keys, proxy tokens, and credentials (like Telegram Bot Tokens and Gmail App Passwords) are managed dynamically via system environments (`os.environ`).
* **Robust Error Handling:** Designed with exception-safe retry mechanisms to handle network drops and layout changes gracefully.
* **Structured Outputs:** Generates clean, production-grade formats (CSV data sheets and formatted `.txt` business reports).

---

## 🚀 Quick Setup & Usage

To run any of the automated suites on your system:

### 1. Set up Environment variables (Security First):
```bash
export SCRAPE_DO_TOKEN="your_proxy_token"
export GMAIL_APP_PASSWORD="your_app_password"
export TELEGRAM_BOT_TOKEN="your_bot_token"
export TELEGRAM_CHAT_ID="your_chat_id"

### 2. Install Dependencies:
```bash
pip install pandas beautifulsoup4 requests lxml

### 3. Execute the Market Analysis Tool:
```bash
python analyze_market.py

---

## 📬 Contact Me for Custom Automations!
Are you looking to automate your business workflow, scrape specific targets, or build smart communication bots? Feel free to reach out or open a pull request!
* **Developer:** Sudhanshu
* **GitHub Profile:** [sudhanshu0-hub](https://github.com/sudhanshu0-hub)
