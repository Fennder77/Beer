import requests

def get_all_beers():#get information about all types of beer.
    url = "https://api.punkapi.com/v2/beers"
    response = requests.get(url)#send a GET request to the specified URL using the requests.get() method, and the result is stored in the response variable.
    beers = response.json()#JSON response transformations
    for beer in beers:#loop through each beer element
        print("ID:", beer['id'])
        print("Name:", beer['name'])

# Call the function to get and display all beers' names and IDs
get_all_beers()