class BookingController:
    def __init__(self, db, booking):
        self.db = db
        self.booking = booking

    def add_booking(self, pin, location_id, room_id, work_place, date_start, date_end):
        db = self.db
        booking = self.booking
        book = booking(pin=pin, card_id='', location_id=location_id, room_id=room_id, work_place=work_place,
                       permanent=0,
                       date_start=date_start, date_end=date_end)
        db.session.add(book)
        db.session.commit()
