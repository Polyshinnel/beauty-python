from app import app
from flask import render_template, request, url_for
from .models import db, DeviceList, DeviceRole, ControllerStatusList, StateList, RoomGroups, Bookings, Users
import json


@app.route('/')
def index():
    data = {'project-info': 'all is works'}
    json_data = json.dumps(data)
    return json_data


@app.route('/authorize', methods=('POST',))
def authorize():
    data = request.form['username']
    return data
