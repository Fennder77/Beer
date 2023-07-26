import requests

def get_single_beer(beer_id):
    url = f"https://api.punkapi.com/v2/beers/{beer_id}"
    response = requests.get(url)
    beer = response.json()[0]
    for key, value in beer.items():
        print(f"{key}: {value}")

get_single_beer(1)
