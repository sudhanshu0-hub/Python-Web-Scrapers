import requests
from bs4 import BeautifulSoup
import csv

# 1. Target URL (E-commerce dummy site)
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

print("🔄 Website se data nikal raha hu, kripya intezar karein...")

# 2. Website ko request bhejna
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 3. Sabhi products ko dhoondhna
    products = soup.find_all('div', class_='thumbnail')
    
    # CSV file likhne ke liye taiyari
    with open('laptops_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Excel ke liye heading (Columns)
        writer.writerow(['Product Name', 'Price', 'Description'])
        
        # 4. Ek-ek product ka data nikalna
        for product in products:
            name = product.find('a', class_='title').text.strip()
            price = product.find('h4', class_='price').text.strip()
            desc = product.find('p', class_='description').text.strip()
            
            # Data ko CSV (Excel) file mein save karna
            writer.writerow([name, price, desc])
            
    print("✅ Kamyabi! Saara data 'laptops_data.csv' file mein save ho gaya hai.")
else:
    print(f"❌ Error: Website nahi khul rahi. Status code: {response.status_code}")
