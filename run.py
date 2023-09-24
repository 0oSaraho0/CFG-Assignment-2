import requests
import random
from random import choice
import datetime
import time
import json
from collections import OrderedDict

# Get Todays Date and arrange strftime display
date_today = datetime.datetime.now()
strftime_date = date_today.strftime("%A %d %B %Y")
# Define Joke  Dictionary
joke_dict = {}
# Define API url
url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&amount=10"

# Add date to Jokes output file
with open("jokes_output.txt", "a") as joke_file:
    joke_file.write("\n" + strftime_date + "\n")


def do_you_want_a_joke():
    """A function to see if the user wants a joke today.
    links to date_today function"""
    want_joke = input("Would you like to hear a joke today? yes/no ").lower()
    if want_joke == "no":
        print("On ok see you another day")
        do_you_want_a_joke()
    elif want_joke == "yes":
        date_today()
    else:
        print(" Sorry I didn't understand please say yes or no")
        do_you_want_a_joke()


def date_today():
    """A function to decide if the user can have a joke today.
    links to get_joke function"""

    with open("jokes_dict.txt", "r") as dict_joke_file:
        content = dict_joke_file.read()
        if strftime_date in content:
            print("oh no you only get one joke a day. Come back again tomorrow")
            do_you_want_a_joke()
        else:
            get_joke()


def get_joke():
    """A function to check if the url request the url and run the data if a 200 code is received.
    links to pick_joke function"""
    # Make API call
    response = requests.get(url)
    if response.status_code != 200:
        print("Oh no! We failed to get a joke this time")
    else:
        # adds response data to the data variable
        global data
        data = response.json()
        pick_joke()


def pick_joke():
    """A function for the user to pick their category and get their joke"""
    joke_dict.update({"Date": strftime_date})
    # Get category from user
    category = input(
        "what category joke do you want to hear? programming, misc, dark, pun, spooky or christmas "
    ).capitalize()
    print(category)
    # check if we have joke in category and add to variable
    jokes_in_category = [
        joke for joke in data["jokes"] if category.lower() == joke["category"].lower()
    ]
    if not jokes_in_category:
        print("oh no we don't have that category this time")
        pick_joke()
    else:
        # Pick a random joke from the category
        random_joke = random.choice(jokes_in_category)
        with open("jokes_output.txt", "a") as joke_file:
            joke_file.write("Your chosen joke category is " + category + "\n")
            joke_dict.update({"Category": category})
        # if statement to check if setup deliver and joke are in joke choice to print correct value
        if "setup" in random_joke and "delivery" in random_joke:
            print(random_joke["setup"])
            # Update dictionary with Setup
            joke_dict.update({"Setup": random_joke["setup"]})
            # Add joke to Jokes output
            with open("jokes_output.txt", "a") as joke_file:
                joke_file.write("Your joke is:" + "\n" + random_joke["setup"] + "\n")
            time.sleep(2)
            print(random_joke["delivery"])
            # Update dictionary with Delivery
            joke_dict.update({"Delivery": random_joke["delivery"]})
            with open("jokes_output.txt", "a") as joke_file:
                joke_file.write(random_joke["delivery"] + "\n")
        elif "joke" in random_joke:
            joke_str = random_joke["joke"]
            # update dictionary with joke
            joke_dict.update({"Joke": joke_str})
            # Splits joke at , and . to make it more readable in console.
            if "." in joke_str:
                joke_split_stop = joke_str.split(".")
                for split_s in joke_split_stop:
                    print(split_s + "\n")
                    with open("jokes_output.txt", "a") as joke_file:
                        joke_file.write(split_s + "\n")
                    # sleep timer to slow joke for better reading.
                    time.sleep(2)
            elif "," in joke_str:
                joke_split_comma = joke_str.split(",")
                for split_c in joke_split_comma:
                    print(split_c + "\n")
                    with open("jokes_output.txt", "a") as joke_file:
                        joke_file.write(split_c + "\n")
                    time.sleep(2)
                    counter = 1


do_you_want_a_joke()

# Add dictionary to file
with open("jokes_dict.txt", "a") as dict_joke_file:
    json.dump(joke_dict, dict_joke_file, indent=2)
