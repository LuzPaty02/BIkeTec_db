class User:
    def __init__(self, user_id, username, matricula, rfid_card_id):
        self.user_id = user_id
        self.username = username
        self.matricula = matricula
        self.rfid_card_id = rfid_card_id

    @staticmethod
    def from_dict(source):
        user = User(
            user_id=source['user_id'],
            username=source['username'],
            matricula=source['matricula'],
            rfid_card_id=source['rfid_card_id']
        )
        return user

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'matricula': self.matricula,
            'rfid_card_id': self.rfid_card_id
        }
