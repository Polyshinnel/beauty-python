from app import app
from flask import render_template, request, url_for
from .models import db, DeviceList, DeviceRole, ControllerStatusList, StateList, RoomGroups, Bookings, Users
import json


@app.route('/')
def index():
    data = {"user2_proximity": 3, "Wifi_1": -80, "Wifi_2": -40, "Wifi_3": -40,
            "thermostat": 18, "light": 0, "hour_of_day": 0, "user3_proximity": 3,
            "user1_proximity": 1, "day_of_week": 1, "security": 0, "minute_of_hour": 9,
            "Act_1": 1, "Act_2": 0, "Act_3": 0}
    json_data = json.dumps(data)
    return json_data
