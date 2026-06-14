import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Quotes aur Authors dono ke tags ko nikalna
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    
    print("\n--- ADVANCED DATA SCRAPED SUCCESSFULLY ---")
    
    # Dono ko ek sath loop mein print karna
    for i in range(5):
        quote_text = quotes[i].text
        author_name = authors[i].text
        print(f"{i+1}. \"{quote_text}\" — By {author_name}\n")
else:
    print("Website open nahi ho rahi hai!")
