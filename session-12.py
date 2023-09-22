import requests
from datetime import datetime
from pprint import pprint as pp

# # this endpoint tells the current location for international space station
# endpoint3 = 'http://api.open-notify.org/iss-now.json'

# response = requests.get(endpoint3)

# data = response.json()
# pp(data)

# timestamp = data['timestamp']
# print(timestamp)


# dt_object = datetime.fromtimestamp(timestamp)

# print("dt_object =", dt_object)
# print("type(dt_object) =", type(dt_object))

# msg = "At {dt} the ISS was passing the following location, latitude: {lat} and longitude: {lon}".format(
#     dt = dt_object,
#     lat = data['iss_position']['latitude'],
#     lon = data['iss_position']['longitude']
# )
# with open('iss_data.txt','a') as text_file:
#     text_file.write(msg + '\n')


# import requests
# from pprint import pprint as pp

# appid = 'ca6407b8a4dd25c116b1f13b62301586'  # key to connect to the API --> create a free account and paste your OWN key here

# endpoint = 'http://samples.openweathermap.org/data/2.5/weather' # see doc to customise your payload

# payload = {
#     'q': 'London,uk',
#     'APPID': appid,
# }

# # response = requests.get('http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=ca6407b8a4dd25c116b1f13b62301586')
# response = requests.get(url=endpoint, params=payload)

# data = response.json()

# print('NAME')
# pp(data['name'])
# print('WEATHER')
# pp(data['weather'])
# print('DATA')
# pp(data)

# # # Write a log record to a file
# # # Run the program multiple times to get more records in the log

pokemon_number = input("What is the Pokemon's ID? ")
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

response = requests.get(url)
print(response)
pokemon = response.json()
# pp(pokemon)

print(pokemon.keys())

name = pokemon['name']
print(name)
height = pokemon['height']
print(height)
weight = pokemon['weight']
print(weight)
# moves = pokemon['move']
pp(pokemon['moves'][0].keys())
for move in pokemon['moves']:
    print(move['move']['name'])
