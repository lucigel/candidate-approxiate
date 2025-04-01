import pickle 
import os
from dotenv import load_dotenv
from Mysql.mysqlhandler import MySQLHandler
# Tải các biến từ tệp .env
load_dotenv()

db_password = os.getenv("db_password")
db_host = os.getenv("localhost")
db_user = os.getenv("db_user")
db_database = os.getenv("db_database")

with open("my_variable.pkl", mode="rb") as f:
    infor_candidate = pickle.load(f)

# Khởi tạo kết nối đến MySQL
mysql_handler = MySQLHandler(host=db_host, database=db_database, user=db_user, password=db_password)

for candidate in infor_candidate:
    mysql_handler.insert_candidate(candidate)

print("Insert Successfully !")