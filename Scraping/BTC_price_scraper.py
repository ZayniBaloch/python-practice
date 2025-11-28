from bs4 import BeautifulSoup
import winsound
import requests
import time

threshold = 0.00001
last_price = None   

while True:
    try:
        btc_html = requests.get("https://www.google.com/finance/quote/BTC-USD?sa=X&ved=2ahUKEwjv8cm0o5WRAxU7T0EAHfm0KUcQ-fUHegQIDRAd").text
        soup = BeautifulSoup(btc_html, "lxml")

        pc = soup.find('div', attrs={'data-source': 'BTC', 'data-target': 'USD'})

        # 1. Get Current Price
        MP = float(pc.get("data-last-price"))
        print(f"Current Price: {MP}")

        # 2. CHECK: Is this the first run?
        if last_price is None:
            print("--> First run. Setting baseline price...")
            # We skip the math because we have nothing to compare to yet.

        else:
            # 3. DO THE MATH (Only if we have a last_price)
            diff = MP - last_price
            percent_change = (diff / last_price) * 100

            print(f"Change: {percent_change:.5f}%")


            # Use abs() so it beeps on CRASHES (negative) too, not just gains
            if abs(percent_change) >= threshold:
                print("🚨 ALERT! BEEPING! 🚨")
                winsound.Beep(1000, 1000)


        last_price = MP
        print("-------------------------------------------")


        time.sleep(10)

    except Exception as e:
        print(f"Error: {e}")
        time.sleep(10)
