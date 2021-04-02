import re
#search and replace
text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"
pattern = re.compile(r'(Mr.|Ms.|Mrs.) [a-z]+',re.I)
# result = pattern.sub("REDACT",text)
# pattern = re.compile(r'(Mr\.|Mrs\.  |Ms\.) [a-z]+',re.I)
# result = pattern.sub("\g<1> replaced-text",text)
result = pattern.sub("replaced-text \g<1>",text)
# pattern = re.compile(r'(Mr.|Mrs.|Ms.) ([a-z])[a-z]+',re.I)
# result = pattern.sub("\g<1> \g<2>",text)
print(result)