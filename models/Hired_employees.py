from flask_app.config import init_app

db = init_app()[1]

class Hired_employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    datetime = db.Column(db.String(50))
    department_id = db.Column(db.Integer)
    job_id = db.Column(db.Integer)
    insert_date = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())