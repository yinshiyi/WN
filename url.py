# url_month = "https://www.southwest.com/air/low-fare-calendar/select-dates.html?adultPassengersCount=1&currencyCode=POINTS&destinationAirportCode=HNL&hasNearByAirport=undefined&lapInfantPassengersCount=0&originationAirportCode=SJC&passengerType=ADULT&promoCode=&returnAirportCode=&selectedFlight1=2023-09-06&selectedFlight2=&tripType=oneway&clk=6403032&cbid=6403032"
# para['fareType'] = ['USD']
import time
from urllib.parse import urlparse, parse_qs, parse_qsl, urlunparse, urlencode
# import webbrowser

# webbrowser.open('https://www.southwest.com')
# Initial URL
url = "https://www.southwest.com/air/booking/select.html?adultPassengersCount=1&departureDate=2023-09-23&departureTimeOfDay=ALL_DAY&destinationAirportCode=SEA&fareType=POINTS&int=LFCBOOKAIR&lapInfantPassengersCount=0&originationAirportCode=OAK&passengerType=ADULT&promoCode=&returnAirportCode=&returnDate=2023-09-24&returnTimeOfDay=ALL_DAY&selectedFlight1=2023-09-23&selectedFlight2=2023-09-24&tripType=roundtrip"

# Parse the URL
o = urlparse(url)
para = parse_qs(o.query)

# Combinations for destinationAirportCode and originationAirportCode
destinations = ['HNL', 'KOA', 'LIH', 'OGG']
origins = ['OAK', 'SJC', 'SFO']

# Generate 9 links
links = []
for dest in destinations:
    for origin in origins:
        # Update the query parameters
        para['destinationAirportCode'] = [dest]
        para['originationAirportCode'] = [origin]

        # Generate the updated URL
        query_string = urlencode(para, doseq=True)
        updated_url = urlunparse([o[0], o[1], o[2], o[3], query_string, o[5]])
        links.append(updated_url)

# Print the generated links
for link in links:
    print(link)


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


for link in links:
    driver = webdriver.Chrome()
    time.sleep(10)

# Launch the browser and navigate to the webpage
    driver.get(link)
