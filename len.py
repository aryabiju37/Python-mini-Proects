nums = [1,34,4,3,4,531,5,4]
len(nums)
#calls nums.__len__() internally
#print("Hello how are you my darling tonight".__len__())

class SpecialList:
	def __init__(self,data):
		self._data = data

	def __len__(self):
		return self._data.__len__() // 2
		pass

l1 = SpecialList([1,2,3,4,5,6,7,8,9,10])

print(len(l1))
