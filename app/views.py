from app import app
from flask import render_template, request, url_for

from .controllers.AuthController import AuthController
from .models import db, DeviceList, DeviceRole, ControllerStatusList, StateList, RoomGroups, Bookings, Users
import json


@app.route('/')
def index():
    data = {'project-info': 'all is works'}
    json_data = json.dumps(data)
    return json_data


@app.route('/authorize', methods=('POST', 'GET'))
def authorize():
    if request.method == 'GET':
        password = request.args['pass']
        username = request.args['user']
        auth_controller = AuthController(db, Users, username=username, password=password)
        token = auth_controller.get_token()
        if token:
            data = {'token': token, 'err': 'none'}
        else:
            data = {'token': False, 'err': 'Ошибка авторизации, неверный логин или пароль'}
        json_obj = json.dumps(data, ensure_ascii=False)
        return json_obj


@app.route('/add-booking', methods=('POST', 'GET'))
def add_booking():
    if request.method == 'GET':
        token = request.args['token']
        auth_controller = AuthController(db, Users)
        check = auth_controller.check_token(token)
        if not check:
            data = {'err': 'Не правильный или истекший токен'}
        else:
            data = {'booking_res': True, 'err': 'none'}

        json_obj = json.dumps(data, ensure_ascii=False)
        return json_obj
