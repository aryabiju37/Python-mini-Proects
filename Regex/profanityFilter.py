import re

def censor(input_string):
    pattern = re.compile(r'\bfrack\w*\b',re.I)
    result = pattern.sub("CENSORED",input_string)
    return result

print(censor("frack you"))