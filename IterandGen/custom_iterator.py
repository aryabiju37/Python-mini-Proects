class Counter:
	def __init__(self,low,high):
		self.current = low
		self.high = high

	def __iter__(self):
		return self

	def __next__(self):
		if self.current < self.high:
			num = self.current
			self.current += 1
			return num
		raise StopIteration





for x in Counter(70,101):
	print(x)