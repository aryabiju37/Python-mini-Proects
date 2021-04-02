#.sort() only used in lists, sorted used in all other datatypes and returns
#a sorted list
users = [
{"user_name":"Samuel","tweets":["I love cake and cats","cats are the best"]},
{"user_name":"Ariel","tweets":["Catleesi"]},
{"user_name":"Sam","tweets":[]},
{"user_name":"mal","tweets":[]},
{"user_name":"el","tweets":[]}
]
lst_sorted_uname = sorted(users,key=lambda usr:usr["user_name"],reverse=True)
print(lst_sorted_uname)

nums=[1,345,123,45,6]
print(max(nums))
print(min(nums))

names = ["Arya","Samson","Ariel","Olivander","Tim"]
print(max(names))
print(min(names))

print(min(len(name) for name in names))
max(names,key=lambda n:len(n))

Songs=[
			{"track_tirtle":"Song1","artist":["Beyonce","Jay Z"],"duration":4.5},
			{"track_tirtle":"Song2","artist":["Katy Perry"],"duration":3.0},
			{"track_tirtle":"I don't care","artist":["JB","Ed Sheeran","Sassy"],"duration":10.0},
			{"track_tirtle":"Song4","artist":["Nathan Wagner","Tom"],"duration":9.0},
			{"track_tirtle":"Song5","artist":["Michael Buble","Kady padry"],"duration":4.25}

	]

print(max(Songs,key=lambda x:len(x["artist"])))	
print(max(Songs,key=lambda x:len(x["artist"]))["track_tirtle"])