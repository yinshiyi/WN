import requests

url = "https://southwest.p.rapidapi.com/flights/SFO/LAX/2020-12-15"
query_params = {
    'currency': 'USD',
    'adults': '1',
    'seniors': '0'
}

headers = {
    'X-RapidAPI-Key': '400ba8630dmshbff9a11d7a32a5ap1c85a9jsn16af3958408e',
    'X-RapidAPI-Host': 'southwest.p.rapidapi.com'
}

try:
    response = requests.get(url, params=query_params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Request failed with status code {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")