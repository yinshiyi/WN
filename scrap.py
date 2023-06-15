from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, date, time, timezone
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--window-size=1920,1080')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome()

# Launch the browser and navigate to the webpage
driver.get("https://www.southwest.com")
from url import all
url = "https://www.southwest.com/air/booking/select.html?adultPassengersCount=1&departureDate=2023-09-23&departureTimeOfDay=ALL_DAY&destinationAirportCode=SEA&fareType=POINTS&int=LFCBOOKAIR&lapInfantPassengersCount=0&originationAirportCode=OAK&passengerType=ADULT&promoCode=&returnAirportCode=&returnDate=2023-09-24&returnTimeOfDay=ALL_DAY&selectedFlight1=2023-09-23&selectedFlight2=2023-09-24&tripType=roundtrip"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")


air-search-results-matrix-0
# Find the table with prices
table = soup.find("table", class_="product_price_info")

if table:
    # Extract the prices
    prices = []
    rows = table.find_all("tr")
    for row in rows:
        cells = row.find_all("td")
        if len(cells) >= 2:
            price = cells[1].text.strip()
            prices.append(price)

    # Print the prices
    for price in prices:
        print(price)
else:
    print("Table not found on the webpage.")
