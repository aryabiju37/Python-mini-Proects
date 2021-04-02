import re

def extract_phone(phone_input):
    phone_regex = re.compile(r"\d{3} \d{3}-\d{4}")
    match = phone_regex.findall(phone_input)
    if match:
        return match
    return None

def isValid_Phone(phone_input):
    phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
    match = phone_regex.findall(phone_input)
    if match:
        return True
    return False
#does the same
# def isValid_Phone(phone_input):
#     phone_regex = re.compile(r"\d{3} \d{3}-\d{4}")
#     match = phone_regex.fullmatch(phone_input)
#     if match:
#         return True
#     return False

print(isValid_Phone("324 908-2345"))
# print(extract_phone("Call me at 234 890-3489 or 324 908-2345"))

# print(extract_phone("Call me at 234 890-3489 or 324 908-2345"))
# print(extract_phone("Call me at 345 998-2349 or 342 978-3479"))
# print(extract_phone("Call me at 384-2498 234-009"))
