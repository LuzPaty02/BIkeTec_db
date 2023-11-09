import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from clases.user import User
from clases.bikes import Bike
from clases.gps import Gps
#from database_connection_files.clases.accessLogs import AccessLog

# Inicializa Firebase con tu archivo de configuración
cred = credentials.Certificate(r"D:\uni - 3\IoT\BIkeTec_db\biketec-d84db-firebase-adminsdk-ys1mt-5772406772.json")
#ruta/a/tu/archivo-de-configuracion.json
firebase_admin.initialize_app(cred)

# Conéctate a Firestore
db = firestore.client()


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


# Ejemplo de cómo crear y agregar instancias de clases a Firestore
def add_data_with_loop():
    # Get the last added user ID from the database
    last_user_id = User.get_last_added_user_id()

    # Initialize the starting user ID for the loop
    starting_user_id = last_user_id + 1 if last_user_id else 1
    for i in range(starting_user_id, starting_user_id + 3):
        # Create new instances of User, Bike, and Gps
        new_user = User(user_id=i, username=f"Usuario prueba {i}", matricula="12345", rfid_card_id=f"RFID{i - 1}")
        new_bike = Bike(bike_id=i, is_available=True, gps_id=i - 1)
        new_gps = Gps(gps_id=i, status=True)

        # Add the instances to the corresponding collections
        add_to_firestore(new_user,"_db")
        add_to_firestore(new_bike,"_db")
        add_to_firestore(new_gps,"_db")

    # Call the function to add data with a loop
add_data_with_loop()

""" 
new_access_log = AccessLog(
    log_id=1,
    user_id=1,
    rfid_card_id="RFID123",
    bike_id=1,
    initial_access_time=None,
    pickup_access_time=None,
    access_type="unlock",
    pickup_latitude=None,
    pickup_longitude=None,
    return_latitude=None,
    return_longitude=None
)

# Add new_access_log to Firestore
add_to_firestore(new_access_log, "access_logs", f"log_{new_access_log.log_id}")

# Define the handle_access_event function
def handle_access_event(collection_name, document_id, user_name, data):
    if data.get('access') is not None:
        if data['access'] == True:
            print(f"Acceso concedido para {user_name}")
        else:
            print(f"Acceso denegado para {user_name}")

# Set up a real-time listener for your access logs
access_logs_ref = db.collection("access_logs")

def on_snapshot(doc_snapshot, changes, read_time):
    for change in changes:
        if change.type.name == "ADDED":
            doc = change.doc.to_dict()
            log_id = change.doc.id
            user_id = doc.get("user_id", "")
            user_name = f"Usuario {user_id}"
            handle_access_event("access_logs", log_id, user_name, doc)

# Watch the access_logs collection
access_logs_watch = access_logs_ref.on_snapshot(on_snapshot) """

# Your code to add new_access_log to Firestore goes here

# ... (The rest of your existing code)

# Cierra la conexión a Firebase
firebase_admin.delete_app(firebase_admin.get_app())
