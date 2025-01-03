from flask import Flask, Blueprint
from .controller import *

user_bp = Blueprint('user', __name__ )
department_bp = Blueprint('department', __name__)

# User routes
user_bp.route('/',  methods=['GET'])(UserController.getUsers)
user_bp.route('/<user_id>',  methods=['GET'])(UserController.getUser)
user_bp.route('/', methods=['POST'])(UserController.addUser)
user_bp.route('/<user_id>', methods=['PUT'])(UserController.editUser)
user_bp.route('/<user_id>', methods=['DELETE'])(UserController.deleteUser)

# User routes
department_bp.route('/',  methods=['GET'])(DepartmentController.getDepartments)
department_bp.route('/<department_id>',  methods=['GET'])(DepartmentController.getDepartment)
department_bp.route('/', methods=['POST'])(DepartmentController.addDepartment)
department_bp.route('/<department_id>', methods=['PUT'])(DepartmentController.editDepartment)
department_bp.route('/<department_id>', methods=['DELETE'])(DepartmentController.deleteDepartment)