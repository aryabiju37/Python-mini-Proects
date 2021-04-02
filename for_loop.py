#how to get the index out of the for loop

lst_flowers = ["Rose","Daisy","Lilly","Lotus","Tulip"]
index = 0
for flower in lst_flowers:
	
	while index < len(lst_flowers):
		index += 1
		print(f"{index }:{ flower}")
		
		break
