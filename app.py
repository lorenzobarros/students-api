from flask import Flask, request, jsonify

app = Flask(__name__)

students = []
current_id = 1


def first_unique_letter(name):
    name = name.lower()
    for letter in name:
        if name.count(letter) == 1:
            return letter
    return "_"


@app.route("/students", methods=["POST"])
def create_student():
    global current_id

    data = request.get_json()
    name = data["name"]
    grade = data["grade"]

    if grade < 0 or grade > 10:
        return jsonify({"error": "Grade must be between 0 and 10"}), 400

    student = {
        "id": current_id,
        "name": name,
        "grade": grade
    }

    students.append(student)
    current_id += 1

    return jsonify(student), 201


@app.route("/students", methods=["GET"])
def get_students():
    result = []

    for student in students:
        result.append({
            "id": student["id"],
            "name": student["name"],
            "grade": student["grade"],
            "first_unique_letter": first_unique_letter(student["name"])
        })

    return jsonify(result)


@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return jsonify({
                "id": student["id"],
                "name": student["name"],
                "grade": student["grade"],
                "first_unique_letter": first_unique_letter(student["name"])
            })

    return jsonify({"error": "Student not found"}), 404


app.run()
