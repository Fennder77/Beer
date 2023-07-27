import requests

def get_single_beer(beer_name):
    url = f"https://api.punkapi.com/v2/beers?beer_name={beer_name}"
    response = requests.get(url)
    beers = response.json()
    if beers:
        beer = beers[0]
        print(f"{beer['name']}\nIngredients:")#using f-string string interpolation
        for ingredient_type, ingredients in beer['ingredients'].items():
            print(f" {ingredient_type.capitalize()}:")
            for ingredient in ingredients:
                name = ingredient['name']
                amount = ingredient['amount']['value']
                unit = ingredient['amount']['unit']
                print(f"  {name}: {amount} {unit}")

get_single_beer("Vice Bier")  # Change "Vice Bier" to any valid beer name you want to retrieve