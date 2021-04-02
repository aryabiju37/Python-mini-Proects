import requests
from termcolor import colored
import pyfiglet

dad_joke = colored(pyfiglet.figlet_format("DAD JOKES 3000"),"cyan")
print(dad_joke)
search_term=input("Let me tell you a joke, gimme a topic: ")

url = "https://icanhazdadjoke.com/search"
response = requests.get(
	url,
	headers={"Accept":"application/json"},
	params={"term":search_term}

	)

data = response.json()
print(data["results"])