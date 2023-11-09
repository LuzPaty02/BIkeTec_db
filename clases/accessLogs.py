class AccessLog:
    def __init__(self, log_id, user_id, rfid_card_id, bike_id, initial_access_time, pickup_access_time, access_type, pickup_latitude, pickup_longitude, return_latitude, return_longitude):
        self._log_id = log_id
        self._user_id = user_id
        self._rfid_card_id = rfid_card_id
        self._bike_id = bike_id
        self._initial_access_time = initial_access_time
        self._pickup_access_time = pickup_access_time
        self._access_type = access_type
        self._pickup_latitude = pickup_latitude
        self._pickup_longitude = pickup_longitude
        self._return_latitude = return_latitude
        self._return_longitude = return_longitude

    # Getter for log_id
    @property
    def get_id(self):
        return self._log_id

    # Setter for log_id
    @get_id.setter
    def log_id(self, value):
        self._log_id = value

    # Getter for user_id
    @property
    def user_id(self):
        return self._user_id

    # Setter for user_id
    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    # Getter for rfid_card_id
    @property
    def rfid_card_id(self):
        return self._rfid_card_id

    # Setter for rfid_card_id
    @rfid_card_id.setter
    def rfid_card_id(self, value):
        self._rfid_card_id = value

    # Add getters and setters for the remaining attributes in a similar way

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
