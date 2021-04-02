import re

def parse_name(input_name):
    pattern = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[a-zA-Z]+) (?P<last>[a-zA-Z]+)$')
    matches = pattern.search(input_name)
    print(matches.group())
    print(matches.group('last'))
    print(matches.group('first'))

parse_name("Ms. Tilda Swinton")