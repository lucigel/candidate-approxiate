import re 

def extract_email(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    
    if emails: 
        return emails[0]  
    return None  

def extract_phone_number(text):
    # Regex để tìm số điện thoại theo các định dạng phổ biến
    phone_pattern = r'\b(?:\+?(\d{1,3})[-.\s]?(\d{1,4})[-.\s]?(\d{3,4})[-.\s]?(\d{3,4})|(?:\d{9,11}))\b'
    potential_numbers = re.findall(phone_pattern, text)
    
    for number in potential_numbers:
        number = ''.join(number)  
        # Loại bỏ các chuỗi có thể là ngày tháng (dd-mm-yyyy hoặc dd/mm/yyyy)
        if not re.match(r'\b\d{1,2}[-/.\s]\d{1,2}[-/.\s]\d{2,4}\b', number):  # Match định dạng ngày
            clean_number = re.sub(r'\D', '', number)  # Loại bỏ các ký tự không phải số
            if len(clean_number) == 10:
                return clean_number
    return "Not Found"




