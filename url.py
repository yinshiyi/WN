# url_month_oneway = "https://www.southwest.com/air/low-fare-calendar/select-dates.html?adultPassengersCount=1&currencyCode=POINTS&destinationAirportCode=HNL&hasNearByAirport=undefined&lapInfantPassengersCount=0&originationAirportCode=SJC&passengerType=ADULT&promoCode=&returnAirportCode=&selectedFlight1=2024-01-01&selectedFlight2=&tripType=oneway&clk=6403032&cbid=6403032"
url_month_oneway = "https://www.southwest.com/air/low-fare-calendar/select-dates.html?adultPassengersCount=1&currencyCode=POINTS&departureDate=2024-01-01&destinationAirportCode=HNL&lapInfantPassengersCount=0&originationAirportCode=SFO&passengerType=ADULT&promoCode=&returnAirportCode=&returnDate=&tripType=oneway"

# url_month_oneway = "https://www.southwest.com/air/low-fare-calendar/select-dates.html?adultPassengersCount=1&cbid=6403032&clk=6403032&currencyCode=POINTS&departureDate=2024-01-01&destinationAirportCode=HNL&hasNearByAirport=undefined&lapInfantPassengersCount=0&originationAirportCode=SJC&passengerType=ADULT&persistNotifications=true&promoCode=&returnAirportCode=&returnDate=&selectedFlight1=2023-09-06&tripType=oneway"
# url_month = "https://www.southwest.com/air/low-fare-calendar/select-dates.html?adultPassengersCount=1&cbid=6403032&clk=6403032&currencyCode=POINTS&departureDate=2024-01-01&destinationAirportCode=HNL&hasNearByAirport=undefined&lapInfantPassengersCount=0&originationAirportCode=OAK&passengerType=ADULT&persistNotifications=true&promoCode=&returnAirportCode=&returnDate=2024-01-01&selectedFlight1=2023-09-23&selectedFlight2=2023-09-24&tripType=roundtrip"
# para['fareType'] = ['USD']
import time
from urllib.parse import urlparse, parse_qs, parse_qsl, urlunparse, urlencode
# import webbrowser

# webbrowser.open('https://www.southwest.com')
# Initial URL
url_single = "https://www.southwest.com/air/booking/select.html?adultPassengersCount=1&departureDate=2023-09-23&departureTimeOfDay=ALL_DAY&destinationAirportCode=SEA&fareType=POINTS&int=LFCBOOKAIR&lapInfantPassengersCount=0&originationAirportCode=OAK&passengerType=ADULT&promoCode=&returnAirportCode=&returnDate=2023-09-24&returnTimeOfDay=ALL_DAY&selectedFlight1=2023-09-23&selectedFlight2=2023-09-24&tripType=roundtrip"


# Parse the URL
o = urlparse(url_month_oneway)
para = parse_qs(o.query,keep_blank_values=True)

# Combinations for destinationAirportCode and originationAirportCode
destinations = ['HNL', 'KOA', 'LIH', 'OGG']
destinations_los = ['LAX', 'ONT', 'BUR', 'SNA','LGB']
destinations_las = ['LAS']
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
with open('links.txt', 'w') as file:
    file.write('\n'.join(links))
  
def generate_and_save_links(destinations, file_name):
    # Generate the links
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
    links.append("\n")
    for dest in origins:
        for origin in destinations:
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

    # Save the links to a file
    with open(file_name, 'w') as file:
        file.write('\n'.join(links))

# Example usage
generate_and_save_links(destinations_las, 'links_las.txt')
generate_and_save_links(destinations_los, 'links_los.txt')



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
