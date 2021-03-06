from . import db


# ORM
class Role(db.Model):
    __tablename__='roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    users = db.relationship('User', backref='role')


class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    passwd = db.Column(db.String, nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))