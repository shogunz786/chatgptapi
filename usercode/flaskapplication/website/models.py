from . import db
class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(20))
    messageType = db.Column(db.String(100))
    message = db.Column(db.String(500))