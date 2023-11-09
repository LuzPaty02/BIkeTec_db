class User:
    current_id = 1
    user_id = 0
    def __init__(self, username, matricula, rfid_card_id, user_id):
        if user_id is None:
            self._user_id = User.current_id
            User.current_id += 1
        else:
            self._user_id = user_id
        self._username = username
        self._matricula = matricula
        self._rfid_card_id = rfid_card_id

    # Getter for user_id
    @property
    def user_id(self):
        return self._user_id

    # Setter for user_id
    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    # Static method to retrieve the last added user ID
    @staticmethod
    def get_last_added_user_id():
        last_user_id = None  # Replace with actual retrieval logic
        return last_user_id

    # Getter for username
    @property
    def username(self):
        return self._username

    # Setter for username
    @username.setter
    def username(self, value):
        self._username = value

    # Getter for matricula
    @property
    def matricula(self):
        return self._matricula

    # Setter for matricula
    @matricula.setter
    def matricula(self, value):
        self._matricula = value

    # Getter for rfid_card_id
    @property
    def rfid_card_id(self):
        return self._rfid_card_id

    # Setter for rfid_card_id
    @rfid_card_id.setter
    def rfid_card_id(self, value):
        self._rfid_card_id = value

    # Factory method to create a User object from a dictionary
    @classmethod
    def from_dict(cls, source):
        user = cls(
            username=source['username'],
            matricula=source['matricula'],
            rfid_card_id=source['rfid_card_id']
        )
        return user

    # Method to convert the User object to a dictionary
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'matricula': self.matricula,
            'rfid_card_id': self.rfid_card_id
        }
