from classroom import db

class Student(db.Model) :
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    surname = db.Column(db.String(length=30), nullable=False)   
    roll = db.Column(db.String(), nullable=False, unique=True)    

    def __repr__(self):
        return self.name+self.surname