students=["Arya","Ambadi","Kanna"]
list2=["Name","Name","Name"]
z = zip(list2,students)
print(list(z))

mid_terms=[80,91,78]
finals=[98,89,67]
final_grades={t[0]:max(t[1],t[2]) for t in zip(students,mid_terms,finals)}

scores = map(lambda pair: max(pair),zip(mid_terms,finals))
print(list(scores))

Finals=dict(
	zip(
	students,
		map(
			lambda pair: max(pair),zip(mid_terms,finals)
		)
	)
)

avg_scores=dict(
	zip(
	students,
	map(
			lambda pair:(pair[0]+pair[1]/2),
			zip(mid_terms,finals)
			)
	)
)
print(avg_scores)

def interleave(str1,str2):
	return ''.join(''.join(x) for x in list(zip(str1,str2)))
	

# print(interleave("hn","io"))

str1="lzr"
str2="iad"
inter = list(zip(str1,str2))
print(inter)
comb_tup=[x[0]+x[1] for x in inter]
print(comb_tup)
str_join = "".join(comb_tup)
print(str_join)





