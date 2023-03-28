from flask import Flask, render_template, jsonify, request
from database import load_students_from_db

app = Flask(__name__)

@app.route("/")
def hello():
  students = load_students_from_db()
  return render_template('home.html', students=students)

@app.route("/api/students")
def student_list():
  students = load_students_from_db()
  return jsonify(students)

@app.route("/student/<id>")
def show_student(id):
  student = load_students_from_db(id)
  return jsonify(student)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
