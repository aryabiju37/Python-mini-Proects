from random import choice

def greet(person):
    def get_mood():
        mood = choice(("Have a nice day","get lost","leave me alone"))
        return mood


    res = get_mood() + " " + person
    return res

print(greet("Andy"))