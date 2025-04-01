import mysql.connector 
from mysql.connector import errors


from datetime import datetime

class MySQLHandler:
    def __init__(self, host, database, user, password):
        try:
            self.connection = mysql.connector.connect(
                host=host, 
                database=database, 
                user=user,
                password=password
            )
            if self.connection.is_connected():
                print("Successfully Connection !!")
        except errors.Error as e:
            print(f"Errors While connecting to MySql: {e}")
            self.connection = None

    def convert_date_format(self, date_str):
        """Chuyển đổi định dạng ngày từ DD/MM/YYYY sang YYYY-MM-DD."""
        if date_str in ['N/A', 'Not specified', '']:
            return None  # Trả về None cho các giá trị không hợp lệ
        try:
            date_obj = datetime.strptime(date_str, '%d/%m/%Y')  # Định dạng DD/MM/YYYY
            return date_obj.strftime('%Y-%m-%d')  # Chuyển đổi sang YYYY-MM-DD
        except ValueError:
            return None  
    
    def insert_candidate(self, candidate_data):
        try:
            cursor = self.connection.cursor()

            # Chèn thông tin ứng viên cùng với học vấn
            insert_candidate_query = """
            INSERT INTO candidates 
                (position,name, address, self_introduction, email, phone, birth, skills, edu, cv_path) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            skills = ''.join(candidate_data['Skills'])  
            birth_date = self.convert_date_format(candidate_data["Birth"])  
            
            education_entries = candidate_data.get("Education", [])
            
            if isinstance(education_entries, str):
                education_info = education_entries
            else:
            # Nếu có nhiều mục học vấn, nối thành chuỗi
                education_info_list = []
                for edu in education_entries:
                    # Xử lý từng mục học vấn và kết hợp vào danh sách
                    degree = edu.get("Degree", "")
                    major = edu.get("Major", "")
                    institution = edu.get("Institution", "")
                    graduation_date = edu.get("Graduation_date", "")
                    education_entry = f"{graduation_date}: {institution}, {major}, {degree}"
                    education_info_list.append(education_entry)
                
                education_info = ' | '.join(education_info_list)


            candidate_info = (
                candidate_data.get("Name", ""),
                candidate_data.get("Address", ""),
                candidate_data.get("Self_introduction", ""),
                candidate_data.get("Email", ""),
                candidate_data.get("Phone", ""),
                birth_date,
                skills,
                education_info  
            )


            cursor.execute(insert_candidate_query, candidate_info)
            candidate_id = cursor.lastrowid  

            # Chèn dự án
            insert_project_query = """
            INSERT INTO projects 
                (candidate_id, project_name, project_technology, project_description) 
                VALUES (%s, %s, %s, %s)
            """
            projects = candidate_data.get("Project", [])
            for project in projects:
                project_info = (
                    candidate_id,
                    project.get("Name_project", ""),
                    project.get("Tool_technology", ""),
                    project.get("Job_descriptions", "")
                )
                cursor.execute(insert_project_query, project_info)

           
            insert_work_experience_query = """
            INSERT INTO work_experiences 
                (candidate_id, company_name, role, working_period) 
                VALUES (%s, %s, %s, %s)
            """
            work_experiences = candidate_data.get("Work_experience", [])
            for work_exp in work_experiences:
                work_exp_info = (
                    candidate_id,
                    work_exp.get("Name_company", ""),
                    work_exp.get("Role", ""),
                    work_exp.get("Working_period", "")
                )
                cursor.execute(insert_work_experience_query, work_exp_info)

            
            self.connection.commit()
            print("Records inserted successfully")

        except errors.Error as e:
            print(f"Error while inserting data: {e}")

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    import os 
    from dotenv import load_dotenv
    load_dotenv()
    db_password = os.getenv("db_password")
    db_host = os.getenv("db_host")
    db_user = os.getenv("db_user")
    db_database = os.getenv("db_database")
    mysql_handler = MySQLHandler(host=db_host, database=db_database, user=db_user, password=db_password)

    

