from app import db
from datetime import datetime


class DeviceList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serial_num = db.Column(db.String(50))
    location_id = db.Column(db.Integer)
    group_room = db.Column(db.Integer)
    room_id = db.Column(db.Integer)
    controller_status = db.Column(db.Integer)
    state = db.Column(db.Integer)
    role = db.Column(db.Integer)
    date_update = db.Column(db.DateTime, default=datetime.utcnow)


class DeviceRole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(50))


class ControllerStatusList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    duration = db.Column(db.Integer)


class StateList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


class RoomGroups(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


class Bookings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pin = db.Column(db.String(50))
    card_id = db.Column(db.String(50))
    location_id = db.Column(db.Integer)
    room_id = db.Column(db.Integer)
    work_place = db.Column(db.Integer)
    permanent = db.Column(db.Integer)
    date_start = db.Column(db.DateTime, default=datetime.utcnow)
    date_end = db.Column(db.DateTime, default=datetime.utcnow)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50))
    passw = db.Column(db.String(50))
    token = db.Column(db.String(50))
    last_enter = db.Column(db.DateTime, default=datetime.utcnow)
