import os
from app import app, db
from app.models import DeviceList, DeviceRole, ControllerStatusList, StateList, RoomGroups, Bookings, Users


def make_shell_context():
    return dict(app=app, db=db, DeviceList=DeviceList, DeviceRole=DeviceRole, ControllerStatusList=ControllerStatusList,
                StateList=StateList, RoomGroups=RoomGroups, Bookings=Bookings, Users=Users)


if __name__ == '__main__':
    app.run()
