from flask import request, jsonify, make_response
from app import db
from app.model import Department

class DepartmentController:

    def getDepartments():
        departments = Department.query.all()
        return jsonify([department.serialize() for department in departments])

    def getDepartment(department_id):
        department = Department.query.get(department_id)
        if department:
            return jsonify(department.serialize())
        return make_response('Department not found', 404)
    
    def addDepartment():
        data = request.get_json()
        new_department = Department(
            shortname=data.get('shortname'),
            fullname=data.get('fullname')
        )
        db.session.add(new_department)
        db.session.commit()
        return DepartmentController.getDepartments()
    
    def editDepartment(department_id):
        department = Department.query.get(department_id)
        if department:
            data = request.get_json()
            department.shortname = data.get('shortname', department.shortname)
            department.fullname = data.get('fullname', department.fullname)
            db.session.commit()
            return DepartmentController.getDepartments()
        return make_response('Department not found', 404)

    
    def deleteDepartment(department_id):
        department = Department.query.get(department_id)
        if department:
            db.session.delete(department)
            db.session.commit()
            return make_response('Department deleted successfully', 200)
        return make_response('Department not found', 404)