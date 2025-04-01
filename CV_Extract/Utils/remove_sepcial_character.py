import re 

def remove_special_character(text):
    return re.sub(r'[^a-zA-Z0-9\s@.-]', '', text)
