from sqlalchemy import *

db_connection = "mysql+pymysql://0rmq3se8b06uvqdcc98d:pscale_pw_myVBESyWBNns5CChQ40ry7YjElp2djiBg6YvITUYCi6@aws.connect.psdb.cloud/outingform?charset=utf8mb4"

engine = create_engine(db_connection, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

with engine.connect() as con:
  result = con.execute(text("select * from students"))
  
  columns = result.keys()
  
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
    
    students = []
    for row in result.all():
      values = {}
      for column, value in zip(columns, row):
        values[column] = value
      students.append(values)
    return students

def load_student_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"SELECT * FROM students WHERE id={id}"))
    row = result.fetchone()
    if row is None:
      return None
    else:
      return dict(row._asdict())

def add_data_to_db(id, data):
  with engine.connect() as conn:
    query = conn.execute(text(f"INSERT INTO datasubmitted (student_name, reg_no, department, email, phone_no, address, leaving_date, arriving_date) VALUES ({student_name}, {reg_no}, {department}, {email}, {phone_no}, {address}, {leaving_date}, {arriving_date})"))

    conn.execute(query, 
                 id=id, 
                 student_name=data['student_name'],
                 reg_no=data['reg_no'],
                 department=data['department'],
                 email=data['email'],
                 phone_no=data['phone_no'],
                 address=data['address'],
                 leaving_date=data['leaving_date'],
                 arriving_date=data['arriving_date']
                )
