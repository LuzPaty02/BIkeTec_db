class User:
    # Class-wide variable to track the next available user ID
    current_id = 1

    def __init__(self, username, matricula, rfid_card_id):
        # Initialize the user ID with the current ID and increment the counter
        self._user_id = User.current_id
        User.current_id += 1

        # Set the user's attributes
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
        # Implement logic to retrieve the last added user ID from the database
        # This could involve querying the users collection for the maximum user ID
        # or using a dedicated counter document
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
