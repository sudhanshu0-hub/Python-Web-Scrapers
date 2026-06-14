import pandas as pd
import os

def generate_business_report():
    csv_file = "laptops_data.csv"
    
    if not os.path.exists(csv_file):
        print(f"❌ Error: {csv_file} file nahi mili!")
        return

    print("🔄 Market Data ka Analysis shuru ho raha hai...")
    
    # CSV file ko load karna
    df = pd.read_csv(csv_file)
    
    # Columns ke aage-piche se space hatana
    df.columns = df.columns.str.strip()
    
    # Exact aapke columns ke naam use karna
    title_col = 'Product Name'
    price_col = 'Price'

    # Price ko clean karke number mein badalna
    df['Clean_Price'] = df[price_col].astype(str).str.replace(r'[^\d]', '', regex=True)
    df['Clean_Price'] = pd.to_numeric(df['Clean_Price'], errors='coerce')
    
    # Empty prices ko drop karna
    df = df.dropna(subset=['Clean_Price'])
    
    if len(df) == 0:
        print("❌ Error: CSV file mein koi valid price data nahi mila!")
        return

    total_laptops = len(df)
    max_price = df['Clean_Price'].max()
    min_price = df['Clean_Price'].min()
    avg_price = df['Clean_Price'].mean()
    
    mahanga_laptop = df[df['Clean_Price'] == max_price][title_col].values[0]
    sasta_laptop = df[df['Clean_Price'] == min_price][title_col].values[0]

    report = f"""
==================================================
📊 SUDHANSHU'S AUTOMATED MARKET RESEARCH REPORT 📊
==================================================
📈 Total Products Analyzed : {total_laptops} Laptops
💵 Average Market Price    : ₹{avg_price:,.2f}
💎 Most Expensive Product  : ₹{max_price:,.2f}
   👉 {str(mahanga_laptop)[:60]}...
💰 Most Affordable Product : ₹{min_price:,.2f}
   👉 {str(sasta_laptop)[:60]}...
==================================================
🔥 TOP 5 BEST VALUE DEALS FOUND (Sorted by Price) 🔥
==================================================
"""
    top_deals = df.sort_values(by='Clean_Price').head(5)
    
    for index, row in top_deals.iterrows():
        report += f"📍 ₹{row['Clean_Price']:,.0f} - {str(row[title_col])[:65]}...\n"
        
    report += "=================================================="
    
    print(report)
    
    with open("Market_Analysis_Report.txt", "w", encoding="utf-8") as f:
        f.write(report)
    print("\n✅ Success: 'Market_Analysis_Report.txt' save ho gayi hai!")

if __name__ == "__main__":
    generate_business_report()
