import time
import pickle
import os
import urllib.parse
from pdf2image import convert_from_path
import pytesseract
from Cohere.response_cohere import cohere_response
from Utils.remove_sepcial_character import remove_special_character
from Utils.remove_extra_whitespace import remove_extra_whitespace
from Utils.infor_candidate_extract import extract_email, extract_phone_number

# Tesseract OCR, pdf2 
def extract_text_tesseract(file_path, dpi=300, lang="eng+vie"):
    extracted_text = ""
    pages = convert_from_path(file_path, dpi=dpi)
    for page in pages:
        text = pytesseract.image_to_string(page, lang=lang)
        extracted_text += text
    
    return extracted_text

current_path = os.getcwd()
base_path = os.path.join(current_path, "CV")

candidate = []

def main():
    for job_name in os.listdir(base_path):
        job_path = os.path.join(base_path, job_name)
        
        for item_candidate in os.listdir(job_path):
            if item_candidate.endswith('.pdf'):
                item_candidate_path = os.path.join(job_path, item_candidate)
                
                text = extract_text_tesseract(item_candidate_path)
                text = remove_extra_whitespace(text)
                text = remove_special_character(text)

                response_cv = cohere_response(cv_text=text, file_path=item_candidate, full_file_path=item_candidate_path)
                
                try:
                    name = response_cv["Name"]
                    birth_date = response_cv["Birth_date"]
                    address = response_cv["Address"]
                    self_introduction = response_cv["Self_introduction"]
                    education = response_cv["Education"]
                    skills = response_cv["Skills"]
                    project = response_cv["Project"]
                    work_experience = response_cv["Work_experience"]
                    cv_path = response_cv["cv_path"]
                    cv_path = f"file:///{urllib.parse.quote(cv_path.replace('\\', '/'))}"
                    email = extract_email(text)
                    phone = extract_phone_number(text)
                    
                    candidate.append({
                        "Position": position,
                        "Name": name, 
                        "Address": address, 
                        "Self_introduction": self_introduction,
                        "Education":education,
                        "Email": email, 
                        "Phone": phone, 
                        "Birth": birth_date, 
                        "Skills": skills,
                        "Project": project, 
                        "Work_experience": work_experience,
                        "Cv_path": cv_path
                    })
                except KeyError as e:
                    
                    print(f"Missing key in the response: {e}")
                

if __name__ =="__main__":
    time_start = time.time()
    main()
    time_end = time.time()
    print(f"Time process is {time_end - time_start} seconds.")

    with open('my_variable.pkl', 'wb') as file:
        pickle.dump(candidate, file)
