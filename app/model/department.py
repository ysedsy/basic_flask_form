from app.database import db

class Department(db.Model):
    __tablename__ = 'departments'
    
    id = db.Column(db.Integer, primary_key=True)
    shortname = db.Column(db.String(50), nullable=False)
    fullname = db.Column(db.String(100), nullable=False)

    def __init__(self, shortname, fullname):
        self.shortname = shortname
        self.fullname = fullname

    def serialize(self):
        return {
            'id': self.id,
            'shortname': self.shortname,
            'fullname': self.fullname
        }

    def __str__(self):
        return f"<Department {self.shortname}>"

    def __repr__(self):
        return f"<Department(id={self.id}, shortname={self.shortname}, fullname={self.fullname})>"