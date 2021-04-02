import re

pattern = re.compile(r"\d{3} \d{3}-\d{4}")
res = pattern.search("Call me at 345 998-2349 or 342 978-3479")
#returns the first match
print(res.group()) 
#returns a list of all the matched items
result_multi = pattern.findall("Call me at 234 890-3489 or 324 908-2345")
print(result_multi)