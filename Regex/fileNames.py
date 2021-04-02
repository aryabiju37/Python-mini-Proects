import re
titles=[
    "Significant Others (1987)",
    "Tales of the City (1978)",
    "Mary Ann in Autumn (2010)",
    "BabyCakes (1984)",
    "Sure of You (1989)",
    "Further Tales of the City (1982)"
]

titles.sort()
fixed_titles = []
# print(titles)
pattern = re.compile(r"(?P<title>^[\w ]+) \((?P<year>\d{4})\)",re.I)
for book in titles:
    fixed_titles.append(pattern.sub("\g<year> - \g<title>",book))
fixed_titles.sort()
print(fixed_titles)
    
