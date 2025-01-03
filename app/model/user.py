from app.database import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.NVARCHAR(50), nullable=False)
    surname = db.Column(db.NVARCHAR(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'age': self.age,
            'department_id': self.department_id
        }

    def __str__(self):
        return f"User {self.name} {self.surname}, Age: {self.age}, Department ID: {self.department_id}"

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, surname={self.surname}, age={self.age}, department_id={self.department_id})>"