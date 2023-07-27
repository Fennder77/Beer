import requests


def get_single_beer(beer_name):
    url = f"https://api.punkapi.com/v2/beers?beer_name={beer_name}"
    response = requests.get(url)
    beers = response.json()
    if beers:
        beer = beers[0]#the first beer from the list of beers
        print(f"{beer['name']}\nIngredients:")#f-string to display the value of the 'name' key from the beer dictionary.
        total_kilograms = 0
        for ingredient_type, ingredients in beer['ingredients'].items():
            print(f" {ingredient_type.capitalize()}:")
            for ingredient in ingredients:
                name = ingredient['name']
                amount = ingredient['amount']['value']
                unit = ingredient['amount']['unit']
                print(f"  {name}: {amount} {unit}")
                if unit == "kilograms":
                    total_kilograms += float(amount)

        print(f"\nTotal amount of ingredients in kilograms: {total_kilograms:.2f} kg")
    else:
        print(f"Beer '{beer_name}' not found.")


get_single_beer("Vice Bier")
