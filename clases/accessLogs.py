class AccessLog:
    def __init__(self, log_id, user_id, rfid_card_id, bike_id, initial_access_time, pickup_access_time, access_type, pickup_latitude, pickup_longitude, return_latitude, return_longitude):
        self.log_id = log_id
        self.user_id = user_id
        self.rfid_card_id = rfid_card_id
        self.bike_id = bike_id
        self.initial_access_time = initial_access_time
        self.pickup_access_time = pickup_access_time
        self.access_type = access_type
        self.pickup_latitude = pickup_latitude
        self.pickup_longitude = pickup_longitude
        self.return_latitude = return_latitude
        self.return_longitude = return_longitude

    @staticmethod
    def from_dict(source):
        access_log = AccessLog(
            log_id=source['log_id'],
            user_id=source['user_id'],
            rfid_card_id=source['rfid_card_id'],
            bike_id=source['bike_id'],
            initial_access_time=source['initial_access_time'],
            pickup_access_time=source['pickup_access_time'],
            access_type=source['access_type'],
            pickup_latitude=source['pickup_latitude'],
            pickup_longitude=source['pickup_longitude'],
            return_latitude=source['return_latitude'],
            return_longitude=source['return_longitude']
        )
        return access_log

    def to_dict(self):
        return {
            'log_id': self.log_id,
            'user_id': self.user_id,
            'rfid_card_id': self.rfid_card_id,
            'bike_id': self.bike_id,
            'initial_access_time': self.initial_access_time,
            'pickup_access_time': self.pickup_access_time,
            'access_type': self.access_type,
            'pickup_latitude': self.pickup_latitude,
            'pickup_longitude': self.pickup_longitude,
            'return_latitude': self.return_latitude,
            'return_longitude': self.return_longitude
        }
