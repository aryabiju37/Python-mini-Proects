names = ["Charlie","Charles","Chammy","Chan","Ciky"]
print(all([name[0]=="C" for name in names]))
names.append("Krawford")
print(all([name[0]=="C" for name in names]))
print(any([name[0]=="K" for name in names]))
nums=[2,4,5,6]
print(any([num%2!=0 for num in nums]))


lst=[2,'a','b']
#point to mote : not list comprehension
print(all(type(l)==str for l in lst))