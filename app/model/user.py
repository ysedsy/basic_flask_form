from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=False)

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