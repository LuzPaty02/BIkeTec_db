""" from clases.user import User
from clases.bikes import Bike
from clases.gps import Gps



# Define a function to add an instance to Firestore
def add_to_firestore(instance, collection_name):
    data = instance.to_dict()
    # Determine the appropriate collection based on the instance type
    if isinstance(instance, User):  
        collection = db.collection(f"{collection_name}_users")
        document_id = f"{collection_name}_{instance.user_id}"
    elif isinstance(instance, Bike):
        collection = db.collection(f"{collection_name}_bikes")
        document_id = f"{collection_name}_{instance.bike_id}"
    elif isinstance(instance, Gps):
        collection = db.collection(f"{collection_name}_gps")
        document_id = f"{collection_name}_{instance.gps_id}"

    # Add the data to the collection
    collection.document(document_id).set(data)

def add_data_with_loop():
    # Get the last added user ID from the database
    last_user_id = User.get_last_user_id()

    # Initialize the starting user ID for the loop
    starting_user_id = last_user_id + 1 if last_user_id else 1


    # Loop through the user IDs, starting from the next one
    for i in range(starting_user_id, starting_user_id + 3):
        # Create new instances of User, Bike, and Gps
        new_user = User(user_id=i, username=f"Usuario prueba {i}", matricula="12345", rfid_card_id=f"RFID{i - 1}")
        new_bike = Bike(bike_id=i, is_available=True, gps_id=i - 1)
        new_gps = Gps(gps_id=i, status=True)

"       # Add the instances to the corresponding collections
        add_to_firestore(new_user, "_db")
        add_to_firestore(new_bike, "_db")
        add_to_firestore(new_gps, "_db") """
    
        # Call the function to add data with a loop