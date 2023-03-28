from sqlalchemy import *

db_connection = "mysql+pymysql://mz6ku5dom65qtox75j5q:pscale_pw_nMQfA30d0IYSNfyqXcX6Vul9zBDzzq9E73a8OUwqgfJ@ap-south.connect.psdb.cloud/rmkforms?charset=utf8mb4"

engine = create_engine(db_connection, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

with engine.connect() as con:
  result = con.execute(text("select * from students"))
  
  columns = result.keys()
  print("Columns:", columns)
  
  result_dicts = []
  for row in result.all():
    row_dict = {}
    for column, value in zip(columns, row):
      row_dict[column] = value
    result_dicts.append(row_dict)

print(result_dicts)

def load_students_from_db():
  with engine.connect() as con:
    result = con.execute(text("select * from students"))
    
    columns = result.keys()
    print("Columns:", columns)
    
    students = []
    for row in result.all():
      values = {}
      for column, value in zip(columns, row):
        values[column] = value
      students.append(values)
    return students
