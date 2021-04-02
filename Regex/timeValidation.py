import re
    def is_valid_time(time_input): 
           
        pattern = re.compile(r"\d{1,2}:\d{1,2}")
        result = pattern.fullmatch(time_input)
        if result:
            return True
        return False
