class Gps:
    def __init__(self, gps_id, status):
        self.gps_id = gps_id
        self.status = status

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
