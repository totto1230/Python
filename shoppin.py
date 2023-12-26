#!/usr/bin/env python3
# Author:  https://github.com/totto1230
# This is a script to identify webstores 

from bs4 import BeautifulSoup
from selenium import webdriver
import emoji
import os

def get_websites():
    # opening the file in read mode, replace 'file_name' with the actual name of your file
    with open('test_webs.txt', 'r') as archivo:
        lineas = archivo.read().splitlines()
    websites = [linea for linea in lineas]
    size=len(websites)
    print(websites)
    print(f"NUMBERS OF WEBSITES GATHERED: {size} "+ emoji.emojize(':thinking_face:'))
    return websites

def get_reaches(all_websites):
    scoped=[]
    not_reach=[]
    print("REVIEWING THE WEBSITES... " + emoji.emojize(':thinking_face:'))
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
    ##TODO:
    ##Add more selectors or/and improve the selection method.
    selectors = [
    'a[href*="cart"]',                     # Matches links with "cart" in href attribute
    'a[href*="minicart-link"]',            # Matches links with "minicart-link" in href attribute
    'li[class*="cart"]',                   # Matches list items with "cart" in class attribute
    'a[class="cart_link"]',                 # Matches links with a specific class "cart_link"
    'a[class_="minicart-link"]',            # Matches links with a specific class "minicart-link"
    'button:contains("Add to Cart")',      # Matches buttons with specific text "Add to Cart"
    'a[class*="minicart-link"]',            # Matches links with "minicart-link" in class attribute
    'a[class*="minicart_link"]',            # Matches links with "minicart_link" in class attribute
    'span:contains("Cart")',                # Matches spans with specific text "Cart"
    '.checkout',                            # Matches elements with class "checkout"
    'div[data-cart]',                       # Matches divs with data-cart attribute
    'button[class*="cart"]',                # Matches buttons with "cart" in class attribute
    'span[class*="cart"]',                  # Matches spans with "cart" in class attribute
    'div[class*="cart"]',                   # Matches divs with "cart" in class attribute
    'input[type="button"][value*="Cart"]', # Matches input buttons with "Cart" in value attribute
    'a:has(img[src*="cart"])',              # Matches links with an image containing "cart" in src attribute
    'a[aria-label*="Cart"]',                # Matches links with "Cart" in aria-label attribute
    'a[aria-label*="Shopping"]',             # Matches links with "Shopping" in aria-label attribute
    'a.minicart-link',
    'div.minicart a.minicart-link',  # Matches cart link
    'a:contains("cart")',
    'div[class*="minicart-link"] a'
    ] 
    combined_selector = ', '.join(selectors)
    i=1
    options = webdriver.ChromeOptions()
    ##Preventing chrome from launching GUI
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
        print('\nSHOPS FOUND: ')
        for shop in shops:
            print(shop + " ✓\n")
    else:
        print("DIDN'T FIND ANYTHING :d \n")
    
    for notr in not_reach:
        print(f"{notr} is not reachable " + " ✕\n")
    print("TOTAL OF WEBSITES NOT REACHABLE: " + str(len(not_reach)) + " \n")       
    
    for noshop in not_shop:
        print(f"{noshop} is not a shop ")


if __name__ == "__main__":
   websites_all = get_websites()
   websites_reach,not_reach= get_reaches(websites_all)
   check_websites(websites_reach,not_reach)