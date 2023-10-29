from flask import Flask, jsonify

app = Flask(__name__)
students = [
        {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
        {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
        {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
        {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
        {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
        {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
        {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
        {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
        {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
        {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
    ]

# Better way

def filter_students(filter_function):
    filtered_students = list(filter(filter_function, students))
    return jsonify(filtered_students)

@app.route('/students', methods=['GET'])
def get_all_students():
    return jsonify(students)

@app.route('/old_students', methods=['GET'])
def get_old_students():
    return filter_students(lambda student: student['age'] > 20)

@app.route('/young_students', methods=['GET'])
def get_young_students():
    return filter_students(lambda student: student['age'] < 21)

@app.route('/advance_students', methods=['GET'])
def get_advance_students():
    return filter_students(lambda student: student['age'] < 21 and student['grade'] == 'A')

@app.route('/student_names', methods=['GET'])
def get_student_names():
    student_names = [{'first_name': student['first_name'], 'last_name': student['last_name']} for student in students]
    return jsonify(student_names)

@app.route('/student_ages', methods=['GET'])
def get_student_ages():
    student_ages = [{'student_name': f"{student['first_name']} {student['last_name']}", 'age': student['age']} for student in students]
    return jsonify(student_ages)

app.run(debug=True)

# @app.route('/students', methods=['GET'])
# def get_all_students():
#     return jsonify(students)

# @app.route('/old_students', methods=['GET'])
# def get_old_students():
#     old_students = []
#     for stud in students:
#         if stud['age'] > 20:
#             old_students.append(stud)
#     return jsonify(old_students)

# @app.route('/young_students', methods=['GET'])
# def get_young_students():
#     young_students = []
#     for stud in students:
#         if stud['age'] < 21:
#             young_students.append(stud)
#     return jsonify(young_students)

# @app.route('/advance_students', methods=['GET'])
# def get_advance_students():
#     advance_students = []
#     for stud in students:
#         if stud['age'] < 21 and stud['grade'] == 'A':
#             advance_students.append(stud)
#     return jsonify(advance_students)

# @app.route('/student_names', methods=['GET'])
# def get_student_names():
#     student_names = []
#     for stud in students:
#         first_name = stud.get('first_name')
#         last_name = stud.get('last_name')
#         student_names.append({'first_name': first_name, 'last_name': last_name})
#     return jsonify(student_names)     

# @app.route('/student_ages', methods=['GET'])
# def get_student_ages():
#     student_ages = []
#     for stud in students:
#         first_name = stud.get('first_name')
#         last_name = stud.get('last_name')
#         age = stud.get('age')
#         student_ages.append({'student_name': first_name + ' ' + last_name, 'age': age})
#     return jsonify(student_ages)

# app.run(debug=True)






