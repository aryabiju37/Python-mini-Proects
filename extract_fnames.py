names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
def extract_names(names):
	full_names = [names[i]['first']+" "+names[i]['last'] for i in range(len(names))]
	print(full_names)

#print(extract_names(names))

def fname(names):
	fullname= list(map(lambda x:"{} {}".format(x["first"],x["last"]),names))
	print(fullname)

print(fname(names))

