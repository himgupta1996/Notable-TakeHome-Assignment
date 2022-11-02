from crypt import methods
from urllib import request
from flask import Blueprint, request, render_template
from .models import Student
import json
from . import db
view1 = Blueprint('view1', __name__)

from flask_expects_json import expects_json

schema = {
    'type': 'object',
    'properties': {
        'firstname': {'type': 'string'},
        'lastname': {'type': 'string'},
        'email': {'type': 'string'}
    },
    'required': ['email', 'firstname']
}

@view1.route('/home')
def index():
	return render_template("index.html", index = True)

@view1.route('/home2')
def index2():
	return "home2"


@view1.route('/', methods = ["GET"])
def get_index():
    print("I am in get")
    students = Student.query.all()
    print(students)
    return "Hello students!"

@view1.route('/', methods = ["POST"])
@expects_json(schema)
def post_index():
    print("I am in post")
    student_data = json.loads(request.data)
    print(student_data)
    print(request.form.get('firstname'))

    new_student = Student(firstname = "Himanshu", lastname = "Gupta")
    db.session.add(new_student)
    db.session.commit()
    students = Student.query.all()
    print(students)

    return "Hello students!"

@view1.route('/create', methods = ["GET", "POST"])
def create_student():
    if request.method == "POST":
        print(request.form['title'])
        print("I am here")
        students = [1,2,3,4]
        return render_template("form.html", students = students)
    else:
        return render_template("form.html")