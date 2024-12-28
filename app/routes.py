from flask import Flask, Blueprint
from .controller import *

user_bp = Blueprint('user', __name__)
department_bp = Blueprint('department', __name__)

@user_bp.route('/user', methods=['GET'])
def get_users():
    return "List of users"

@user_bp.route('/user', methods=['POST'])
def create_user():
    return "Create a new user"

@department_bp.route('/department', methods=['GET'])
def get_departments():
    return "List of departments"

@department_bp.route('/department', methods=['POST'])
def create_department():
    return "Create a new department"