import re

def parse_date(input_date):
# [D]an - Matches “Dan”, not very useful.
# [DB]an - Matches “Dan” and “Ban” (first letter can be "D" or "B").
    parsed_date = re.compile(r"^(?P<date>\d\d)[/,.](?P<month>\d\d)[/,.](?P<year>\d{4})$")
    matches = parsed_date.search(input_date)
    if matches:
            
        return {"d":matches.group("date"),
        "m":matches.group("month"),
        "y":matches.group("year")
        }
    else:
        return None


