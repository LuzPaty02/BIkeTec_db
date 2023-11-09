class Bike:
    current_bike_id = 0
    bike_id = 0
    def __init__(self, bike_id, is_available, gps_id):
        if bike_id is None:
            self._bike_id = Bike.current_bike_id
            Bike.current_bike_id += 1
        else:
            self._bike_id = bike_id
        self._is_available = is_available
        self._gps_id = gps_id

    # Getter for bike_id
    @property
    def bike_id(self):
        return self._bike_id

    # Setter for bike_id
    @bike_id.setter
    def bike_id(self, value):
        self._bike_id = value
    
    @staticmethod
    def get_last_added_bike_id():
        last_bike_id = None
        return last_bike_id

    # Getter for is_available
    @property
    def is_available(self):
        return self._is_available

    # Setter for is_available
    @is_available.setter
    def is_available(self, value):
        self._is_available = value

    # Getter for gps_id
    @property
    def gps_id(self):
        return self._gps_id

    # Setter for gps_id
    @gps_id.setter
    def gps_id(self, value):
        self._gps_id = value

    @staticmethod
    def from_dict(source):
        bike = Bike(
            bike_id=source['bike_id'],
            is_available=source['is_available'],
            gps_id=source['gps_id']
        )
        return bike

    def to_dict(self):
        return {
            'bike_id': self.bike_id,
            'is_available': self.is_available,
            'gps_id': self.gps_id
        }
