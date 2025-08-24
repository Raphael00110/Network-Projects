import requests
import time
import json
from useful import Loader, ClearScreen
import msvcrt

url = "https://api.coingecko.com/api/v3/coins/markets"


while True:
 try:
    ClearScreen.clear()
    print("----Welcome to the Crypto Market Viewer!----\n\n\n")
    ask = input("1- View Top Coins\n2- Search Coin\n3- Exit\nChoose an option: ")
    ClearScreen.clear()
    if ask == '1':
        try:
            prompt = int(input("How Many Coins Do You Want to See?:  "))
            if prompt <= 0:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            msvcrt.getch()
            continue
        Loader.loading("Loading")
        ClearScreen.clear()
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": prompt,
            "page": 1,
            "sparkline": False
        }
        response = requests.get(url, params=params, timeout=5)
        if response.status_code == 200:
            data = response.json()
            for coin in data:
                print("-" * 40)
                print(f"{coin['name']} ({coin['symbol'].upper()}): ${coin['current_price']:.2f} | 24h: {coin['price_change_percentage_24h']:.2f}%")
            print("Press any key to continue...")
            msvcrt.getch()
            continue

        
        else:
            print("Failed to fetch data. Status code:", response.status_code)
    elif ask == '2':
        coin_name = input("Enter the coin name: ").title()
        Loader.loading("Searching")
        ClearScreen.clear()
        params = {
            "vs_currency": "usd",
            "ids": coin_name,
            "order": "market_cap_desc",
            "per_page": 1,
            "page": 1,
            "sparkline": False
        }
        response = requests.get(url, params=params, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data:
                coin = data[0]
                print("-" * 40)
                print(f"{coin['name']} ({coin['symbol'].upper()}): ${coin['current_price']:.2f} | 24h: {coin['price_change_percentage_24h']:.2f}%")
                print("-" * 40)
                print("Press any key to continue...")
                msvcrt.getch()
            else:
                print("Coin not found.")
                print("Press Any Key to continue ")
                msvcrt.getch()
                ClearScreen.clear()
                continue
        else:
            print("Failed to fetch data. Status code:", response.status_code)
            time.sleep(1.5)
            ClearScreen.clear()
    elif ask == '3':
        Loader.loading("Exiting")
        break
    else:
        print("Invalid option. Please try again. Press Any Key to continue...")
        msvcrt.getch()
        time.sleep(1)
        ClearScreen.clear()
        continue
 except KeyboardInterrupt:
    print("Error!")
    Loader.loading("\nExiting...")
    break
 except requests.exceptions.RequestException as e:
    print("Network error:", e)
    Loader.loading("\nExiting...")
    break
    


        
    
