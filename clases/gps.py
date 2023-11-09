class Gps:
    current_gps_id = 0

    def __init__(self, status):
        # Initialize the GPS ID with the current ID and increment the counter
        self._gps_id = Gps.current_gps_id
        Gps.current_gps_id += 1

        # Set the GPS's status
        self._status = status

    # Getter for gps_id
    @property
    def gps_id(self):
        return self._gps_id

    # Setter for gps_id
    @gps_id.setter
    def gps_id(self, value):
        self._gps_id = value
    
    @staticmethod
    def get_last_added_gps_id():
        last_gps_id = None
        return last_gps_id


    # Getter for status
    @property
    def status(self):
        return self._status

    # Setter for status
    @status.setter
    def status(self, value):
        self._status = value

    @staticmethod
    def from_dict(source):
        gps = Gps(
            gps_id=source['gps_id'],
            status=source['status']
        )
        return gps

    def to_dict(self):
        return {
            'gps_id': self.gps_id,
            'status': self.status
        }
