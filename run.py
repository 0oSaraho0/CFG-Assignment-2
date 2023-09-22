import requests
import random
from random import choice
from pprint import pprint as pp
import datetime
import time

# Define API url

date = datetime.datetime.now()


url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&amount=10"


with open('jokes_output.txt','a') as joke_file:
    joke_file.write('\n' + date.strftime("%A %d %B %Y") + '\n')

print(date.strftime("%A %d %B %Y"))


""" A function to check if the url request the url and run the data if a 200 code is received """
def get_joke():
    # Make API call
    response = (requests.get(url))
    print(response.status_code)
    if response.status_code != 200:
        print('Oh no! We failed to get a joke this time')
    else:
        global data
        data = response.json()
        pp(data)
    pick_joke()



# print(jokes)

def pick_joke():
    
    category = input('what category joke do you want to hear? programming, misc, dark, pun, spooky or christmas ').capitalize()
    print(category)

    jokes_in_category  = [joke for joke in data['jokes'] if category.lower() == joke['category'].lower()]
    print(jokes_in_category)   

    if not jokes_in_category:
        print("oh no we don't have that category this time") 
        pick_joke()
    else: 
        random_joke = random.choice(jokes_in_category)
        with open('jokes_output.txt', 'a') as joke_file:
            joke_file.write("Your chosen joke category is " + category + "\n")
        
        if 'setup' in random_joke and 'delivery' in random_joke:
            print(random_joke['setup'])            
            with open('jokes_output.txt', 'a') as joke_file:
                joke_file.write("Your joke is:" + "\n" + random_joke['setup'] + "\n")
            time.sleep(3)
            print(random_joke['delivery'])
            with open('jokes_output.txt', 'a') as joke_file:
                joke_file.write(random_joke['delivery'] + "\n")
        elif 'joke' in random_joke:
            joke_str = (random_joke['joke'])
            if '.' in joke_str:
                joke_split_stop = joke_str.split('.')
                for split_s in joke_split_stop:
                    print(split_s + '\n')
                    with open('jokes_output.txt', 'a') as joke_file:
                        joke_file.write(split_s + "\n")
                    time.sleep(3)
            elif ',' in joke_str:
                joke_split_comma = joke_str.split(',')
                for split_c in joke_split_comma:
                    print(split_c + '\n')
                    with open('jokes_output.txt', 'a') as joke_file:
                        joke_file.write(split_c + "\n")
                    time.sleep(3)
            

get_joke()
