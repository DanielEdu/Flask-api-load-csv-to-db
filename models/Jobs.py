from flask_app.config import init_app

db = init_app()[1]

class Jobs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.String(50))
    insert_date = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())