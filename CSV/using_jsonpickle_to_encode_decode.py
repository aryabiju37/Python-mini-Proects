import jsonpickle

class Cat:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def meows(self):
        print(f"{self.name} meows!!!")

c = Cat("Chacha","Persian")
# j_encoded = jsonpickle.encode(c)
# print(j_encoded)
#result:-{"py/object": "__main__.Cat", "name": "Chacha", "breed": "Persian"}

#helps us to encode data and send it to another language like javascript etc


#encoding into json objects into a .json file just like pickling
# with open("cats.json","w") as file:
#     j_encoded = jsonpickle.encode(c)
#     file.write(j_encoded)

with open("cats.json","r") as file:
    contents = file.read()
    j_decoded_class_obj = jsonpickle.decode(contents)
    print(j_decoded_class_obj.meows())