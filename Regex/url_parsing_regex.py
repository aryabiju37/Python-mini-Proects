import re

url_regex = re.compile(r'(https?)://(www\.[a-zA-Z-0-9]+\.[a-zA-Z]{2,6})/([a-zA-Z0.9-_#@!%^&*$+=?/><\[\]\"\']*)')
match = url_regex.search("https://www.youtube.com/results?search_query=simple+ken")
print(match.group())
#same as above
print(match.group(0))
print(match.group(1))
print(match.group(2))
print(match.group(3))
#below returns a tuple 
print(match.groups()) 
