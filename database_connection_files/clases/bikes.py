class Bike:
    def __init__(self, bike_id, is_available, gps_id):
        self.bike_id = bike_id
        self.is_available = is_available
        self.gps_id = gps_id

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
