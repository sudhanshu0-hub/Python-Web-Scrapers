import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = "http://quotes.toscrape.com/"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('span', class_='text')
        authors = soup.find_all('small', class_='author')
        
        print("--- Aaj Ke Quotes ---")
        for i in range(5):
            print(f"{i+1}. \"{quotes[i].text}\" - By {authors[i].text}\n")
    else:
        print("Website connect nahi ho payi!")

if __name__ == "__main__":
    scrape_quotes()
