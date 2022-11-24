from app import db
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(55),nullable=False)
    email = db.Column(db.String(100),nullable=False,unique=True)
    passsword = db.Column(db.String(500),nullable=False)


class MobileNumber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_number = db.Column(db.String(100),nullable=False)
    zone = db.Column(db.String(100),nullable=False)
    customer_call_time = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    # def __repr__(self):
    #     return f"User('{self.customer_number}','{self.zone}',,'{self.customer_call_time}')"

class TotalGift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gift = db.Column(db.String(100),nullable=False)
    gift_qantity = db.Column(db.String(100),nullable=False)
    # customer_call_time = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

    def __repr__(self):
        return f"User('{self.gift}','{self.gift_qantity}',)"

class PreviousMobileNumbers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    MobileNumber = db.Column(db.String(100),nullable=False)
    # gift_qantity = db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return f"PreviousMobileNumbers('{self.MobileNumber}',)"

class DATA(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    who = db.Column(db.String(100),nullable=False)
    ChannellD = db.Column(db.String(100),nullable=False)
    circle = db.Column(db.String(100),nullable=False)
    operator = db.Column(db.String(100),nullable=False)
    datetim  = db.Column(db.String(100),nullable=False)

    def __repr__(self):
        return f"User('{self.id}','{self.who}','{self.ChannellD}','{self.circle}','{self.operator}','{self.datetim}')"

