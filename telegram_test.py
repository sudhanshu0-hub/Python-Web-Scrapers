import requests

CHAT_ID = "845580463"
tokens = [
    "8948830066:AAEWU-Wu9GQzTJuYow41pVkL4fEhaYy1Y3E",  # Option 1: Number One (Yeh sahi hona chahiye)
    "8948830066:AAEWU-Wu9GQzTJuYow41pVkL4fEhaYyIY3E",  # Option 2: Capital I
    "8948830066:AAEWU-Wu9GQzTJuYow41pVkL4fEhaYylY3E"   # Option 3: Small l
]

print("--- Testing Telegram Tokens ---")
for i, token in enumerate(tokens, 1):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": f"Sudhanshu! Option {i} kamyab raha! 🔥"}
    res = requests.post(url, json=data)
    if "ok\":true" in res.text:
        print(f"✅ Option {i} SUCCESS! Check your Telegram!")
        break
    else:
        print(f"❌ Option {i} Failed (Unauthorized)")
