from urllib.parse import urlparse, parse_qs, parse_qsl, urlunparse, urlencode

url = "https://www.southwest.com/air/booking/select.html?adultPassengersCount=1&departureDate=2023-09-23&departureTimeOfDay=ALL_DAY&destinationAirportCode=SEA&fareType=POINTS&int=LFCBOOKAIR&lapInfantPassengersCount=0&originationAirportCode=OAK&passengerType=ADULT&promoCode=&returnAirportCode=&returnDate=2023-09-24&returnTimeOfDay=ALL_DAY&selectedFlight1=2023-09-23&selectedFlight2=2023-09-24&tripType=roundtrip"
url_month = "https://www.southwest.com/air/low-fare-calendar/select-dates.html?adultPassengersCount=1&currencyCode=POINTS&destinationAirportCode=HNL&hasNearByAirport=undefined&lapInfantPassengersCount=0&originationAirportCode=SJC&passengerType=ADULT&promoCode=&returnAirportCode=&selectedFlight1=2023-09-06&selectedFlight2=&tripType=oneway&clk=6403032&cbid=6403032"
o = urlparse(url)
para = parse_qs(o.query)

para['fareType'] = ['USD']
para['destinationAirportCode'] = ['HNL','KOA','LIH']
para['originationAirportCode'] = ['OAK','SJC','SFO']

query_string = urlencode(para,doseq=True)

updated_url = urlunparse([o[0], o[1], o[2], o[3], query_string, o[5]])
print(updated_url)
