
#json module provides methods to encode/decode python into json
import json
j = json.dumps(["bar",{"foo":("baz",None,1.0,2)}])
print(j)

#result-->["bar", {"foo": ["baz", null, 1.0, 2]}]


#using dumps to convert python class objects:
class Cat:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

c = Cat("Charlie","Taby")

jas = json.dumps(c.__dict__)
print(jas)

#Result:-{"name": "Charlie", "breed": "Taby"}