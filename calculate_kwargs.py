# calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
# calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
#"{} {}".format(kwargs.get("message","The result is"),int(value))
# def calculate(make_float,operation,message,first,second):
def find_value(operation,kwargs):
	if operation=="add":
		return kwargs.get("first",0)+kwargs.get("second",0)
	elif operation=="subtract":
		return kwargs.get("first",0)-kwargs.get("second",0)
	elif operation=="multiply":
		return kwargs.get("first",0)*kwargs.get("second",0)
	elif operation=="divide":
		return kwargs.get("first",0)/kwargs.get("second",1)
	else:
		return 0


def calculate(**kwargs):
	
	value = find_value(kwargs["operation"],kwargs)
	is_float = kwargs.get("make_float",False)
	if is_float:
		msg = "{mesg} {val}".format(mesg=kwargs.get("message","The result is "),val=float(value))
		
	else:
		msg = "{mesg} {val}".format(mesg=kwargs.get("message","The result is "),val=int(value))
	print(msg)

calculate(make_float=True, operation='divide', first=3.5, second=5)
# calculate(make_float=False, operation='add', message='You just added', first=2, second=4)

