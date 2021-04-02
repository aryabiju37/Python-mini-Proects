import re
def parse_bytes(inputStream):
        
    byteStream = re.compile(r'[0-1]{4,}')
    match = byteStream.findall(inputStream)
    return match

print(parse_bytes("11010101 101 323"))
print(parse_bytes("my data is: 10101010 11100010"))
print(parse_bytes("asdsa"))
