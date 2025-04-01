from langchain_community.utilities.sql_database import SQLDatabase

from langchain_google_genai import GoogleGenerativeAI

from dotenv import load_dotenv
import re
import os

load_dotenv()

# connect to My database
db_password = os.getenv("db_password")
db_host = os.getenv("db_host")
db_user = os.getenv("db_user")
db_database = os.getenv("db_name")

llm = GoogleGenerativeAI(google_api_key=os.environ['GOOGLE_API_KEY'], temperature=0.6, model="gemini-1.5-pro-latest")

DB_URI = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_database}"
db = SQLDatabase.from_uri(DB_URI)

# This prompt allow AI query to database
PROMPT = """
    Bạn là một trợ lý AI chuyên truy vấn cơ sở dữ liệu MySQL. 
    Bạn sẽ nhận được câu hỏi từ người dùng và sẽ tạo câu lệnh SQL phù hợp để lấy dữ liệu từ database. 
    Chỉ Trả về câu lệnh SQL cần truy vấn.

    Dưới đây là cấu trúc database:
    - candidates: (id, name, address, self_introduction, email, phone, birth, skills, edu)
    - projects: (id, candidate_id, project_name, project_technology, project_description)
    - work_experiences: (id, candidate_id, company_name, role, working_period)

    Hãy tạo SQL phù hợp
"""

query = "Bạn thấy ứng viên nào ứng tuyển vị trí Tester tiềm năng"  # Hoặc nhập từ người dùng
response = llm.invoke(PROMPT + query)
sql_query = response  
clean_sql_query = re.sub(r"```(sql)?", "", sql_query).strip()

result = db.run(clean_sql_query)  # run sql 
print(result)  