from flask import request, jsonify, make_response
from app import db
from app.model import User

class UserController:

    def getUsers():
        users = User.query.all()
        print("AAA")
        return jsonify([user.serialize() for user in users])

    def getUser(user_id):
        user = User.query.get(user_id)
        if user:
            return jsonify(user.serialize())
        return make_response('User not found', 404)

    
    def addUser():
        data = request.get_json()
        new_user = User(
            name=data.get('name'),
            surname=data.get('surname'),
            age=data.get('age'),
            department_id=data.get('department_id')
        )
        db.session.add(new_user)
        db.session.commit()
        return make_response('User added successfully', 201)

    
    def editUser(user_id):
        user = User.query.get(user_id)
        if user:
            data = request.get_json()
            user.name = data.get('name', user.name)
            user.surname = data.get('surname', user.surname)
            user.age = data.get('age', user.age)
            user.department_id = data.get('department_id', user.department_id)
            db.session.commit()
            return make_response('User updated successfully', 200)
        return make_response('User not found', 404)

    
    def deleteUser(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response('User deleted successfully', 200)
        return make_response('User not found', 404)