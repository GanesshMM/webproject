from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

STUDENTS = [
  {
    'id' : 1,
    'name' : 'Student 1',
    'department' : 'cse',
    'year' : 2
  },
  {
    'id' : 2,
    'name' : 'Student  2',
    'department' : 'ece',
    'year' : 3
  },
  {
    'id' : 3,
    'name' : 'Student 3',
    'department' : 'ai&ds',
    'year' : 1
  },
  {
    'id' : 4,
    'name' : 'Student 4',
    'department' : 'cyber',
    'year' : 4
  }
]

@app.route("/")
def hello():
  return render_template('home.html')


@app.route("/api/students")
def student_list():
  return jsonify(STUDENTS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
