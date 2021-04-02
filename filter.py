names = ["austin","arya","pumpkin","stupid fuck","shyam"]
a_names = list(filter(lambda x:x[0][0]=="a",names))
print(a_names)
names=["Lassie","Colt","Passandra"]
updated_names=list(map(lambda name:f"Your instructor is {name}",filter(lambda val:len(val)>5,names)))
print(updated_names)


#so duplicate key error arises onlhy when we use dict to create a dictionary
users = [
{"user_name":"Samuel","tweets":["I love cake and cats","cats are the best"]},
{"user_name":"Ariel","tweets":["Catleesi"]},
{"user_name":"Sam","tweets":[]},
{"user_name":"mal","tweets":[]},
{"user_name":"el","tweets":[]}
]
user_names=list(map(lambda user : user["user_name"].upper(),filter(lambda usr:not usr["tweets"],users)))
print(user_names)

lst=[-3,-2,0,1,2,4,2,5]
nonneg=list(filter(lambda x:x>=0,lst))
print(nonneg)
