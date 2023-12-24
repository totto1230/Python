#!/usr/bin/env python3
from bs4 import BeautifulSoup
from selenium import webdriver
import emoji
import os

#ref: https://stackoverflow.com/questions/55405590/determining-if-a-website-is-a-web-store-or-not


def get_websites():
    # opening the file in read mode 
    with open('websites.txt', 'r') as archivo:
        lineas = archivo.read().splitlines()
    websites = [linea for linea in lineas]
    size=len(websites)
    print(websites)
    print(f"NUMBERS OF WEBSITES GATHERED: {size}"+ emoji.emojize(':thinking_face:'))
    return websites

def get_reaches(all_websites):
    scoped=[]
    not_reach=[]
    print("REVIEWING THE WEBSITES..." + emoji.emojize(':thinking_face:'))
    for url in all_websites:
        response = os.system("ping -c 1 " + url + " > /dev/null 2>&1")
        if response == 0:
            scoped.append("https://" + url)
        else:
            not_reach.append(url)
    return scoped,not_reach


def check_websites(websites_heal,web_notrec):
    shops = []
    not_reach=web_notrec
    not_shop=[]
    selectors = [
    'a[href*="cart"]',           # Links with "cart" in href attribute
    'li[class*="cart"]',         # List items with "cart" in class attribute
    'a[class="cart_link"]',      # Links with a specific class "cart_link"
    'button:contains("Add to Cart")',  # Buttons with specific text
    #'[id*="cart"]',              # Elements with "cart" in the ID attribute
    'span:contains("Cart")',     # Spans with specific text
    '.checkout',                 # Elements with class "checkout"
    'div[data-cart]']            # Divs with a data attribute related to the cart
    combined_selector = ', '.join(selectors)
    i=1
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('window-size=1200x600')  # Set a small window size
    options.add_argument('log-level=3')
    options.add_argument('window-size=1200x600')  # Set a small window size
    options.add_argument('--headless')  # Explicitly set headless mode
    options.add_argument('--disable-gpu')  # Disable GPU accelerationwebsites_heal
    options.add_argument('--disable-software-rasterizer')
    with webdriver.Chrome(options=options) as driver:
        for url in websites_heal:
            try: 
               print(f"PROCESSING {url} #: "+ str(i) + " of " + str(len(websites_heal)) + "\n")
               i+=1             
            except:
                print(f"Skipped: {url}")
                not_reach.append(url)
                continue
            try:
                driver.get(url)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                items = soup.select(combined_selector)
                if len(items) > 0:
                   shops.append(url)
                else:
                    not_shop.append(url)
            except Exception as ex: 
                print(f"Skipped: {url} due to: " + str(ex))
               
    os.system('clear||cls')
    print("RESULTS: \n")
    if len(shops) > 0:
        print('\nSHOPS FOUND:')
        for shop in shops:
            print(shop + "✓\n")
    else:
        print("DIDN'T FIND ANYTHING :d")
    
    for notr in not_reach:
        print(f"{notr} is not reachable " + "✕\n")
    print("TOTAL OF WEBSITES NOT REACHABLE: " + str(len(not_reach)) + " \n")       
    
    for noshop in not_shop:
        print(f"{noshop} is not a shop")




websites_all = get_websites()
websites_reach,not_reach= get_reaches(websites_all)
check_websites(websites_reach,not_reach)