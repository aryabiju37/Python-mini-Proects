# for x in range(3):
# 	for i in range(1,11):
# 		print("\U0001f626"*i)

for num in range(1,11):
	count = 1
	smileys = ""
	while count <= num:
		smileys += "\U0001f606"
		count += 1
	print(smileys)
