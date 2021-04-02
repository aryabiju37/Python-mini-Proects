import requests
from termcolor import colored
import pyfiglet
import random

dad_joke = colored(pyfiglet.figlet_format("DAD JOKES 3000"),"cyan")
print(dad_joke)
search_term=input("Let me tell you a joke, Give me a topic? ")

url = "https://icanhazdadjoke.com/search"
response = requests.get(
	url,
	headers={"Accept":"application/json"},
	params={"term":search_term}

	)

data = response.json()
joke_results = data["results"]
num_jokes = len(joke_results)
# print(data["results"][num_jokes-1]["joke"])

if(joke_results):
	dict_num = random.randint(0,num_jokes-1)
	print(f"I have got {num_jokes} about {search_term}. Here's One :")
	print(joke_results[dict_num]["joke"])
else:
	print(f"Sorry, I do not have the jokes on {search_term} ")



