def combine_words(word,**kwargs):
	if(kwargs):
		for key,val in kwargs.items():
			if key=="suffix":
				print(word+val) 
			elif key=="prefix":
				print(val+word)
	else:
		print(word)
combine_words("child",prefix="man")
combine_words("child",suffix="ish")
combine_words("child")

def comb_words(word,**kwargs):
	if "prefix" in kwargs:
		return kwargs["prefix"]+word
	elif "suffix" in kwargs:
		return word+kwargs["suffix"]
	return word

print(comb_words("child",prefix="man"))
print(comb_words("child",suffix="ish"))
print(comb_words("child"))

#orders of parameters
#params,args,default params,kwargs
def display(a,b,*args,instructor="Arya",**kwargs)