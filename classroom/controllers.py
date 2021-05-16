from operator import methodcaller

from flask.globals import session
from classroom import app, db
from flask import jsonify, request
from classroom.models import Student

@app.route('/')
def home() :
    res = {
        "status" : "success",
        "message" : "Server running" 
    }
    return jsonify(res)


@app.route('/students', methods=["GET", "POST"])
def students():
    if request.method=="GET":
        students = []
        for st in Student.query.all() :
            students.append({
                "id" : st.id,
                "name" : st.name,
                "surname" : st.surname, 
                "roll" : st.roll
            })
        res = {
            "status" : "success",
            "data" : students,
            "length" : len(Student.query.all())
        }
    else :
        data = request.get_json()
        s = Student(**data)
        db.session.add(s)
        db.session.commit()
        res = {
            "status" : "success",
            "message" : "Student saved to the database" 
        }
    return jsonify(res)


@app.route('/student/<id>', methods=["GET", "PUT", "DELETE"])
def student(id):
    if request.method=="GET":
        st = Student.query.filter_by(id=id).first()
        student  = {
            "id" : st.id,
            "name" : st.name,
            "surname" : st.surname, 
            "roll" : st.roll
        }
        res = {
            "status" : "success", 
            "data" : student
        }
    elif request.method=="PUT":
        data = request.get_json()
        st = Student.query.filter_by(id=id).first()
        st.name = data['name']
        st.surname = data['surname']
        db.session.commit()
        res = {
            "status" : "success",
            "message" : "Student updated in database" 
        }
    else : 
        st = Student.query.filter_by(id=id).first()
        db.session.delete(st)
        db.session.commit()
        res = {
            "status" : "success",
            "message" : "Student deleted" 
        }
    
    return jsonify(res)