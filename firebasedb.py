import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from clases.user import User
from clases.bikes import Bike
from clases.gps import Gps
#from database_connection_files.clases.accessLogs import AccessLog

# Inicializa Firebase con tu archivo de configuración
cred = credentials.Certificate(r" ")
#ruta/a/tu/archivo-de-configuracion.json
firebase_admin.initialize_app(cred)

# Conéctate a Firestore
db = firestore.client()

# Define una función genérica para agregar una instancia de clase a Firestore
def add_to_firestore(instance, collection_name, document_id):
    data = instance.to_dict()  # Use the to_dict() method instead of __dict__
    db.collection(collection_name).document(document_id).set(data)



# Ejemplo de cómo crear y agregar instancias de clases a Firestore
new_user = User(user_id=2, username="Usuario prueba 2", matricula="12345", rfid_card_id="RFID123")
add_to_firestore(new_user, "my_collection", f"user_{new_user.user_id}")

new_bike = Bike(bike_id=2, is_available=True, gps_id=1)
add_to_firestore(new_bike, "my_collection", f"bike_{new_bike.bike_id}")

new_gps = Gps(gps_id=2, status=True)
add_to_firestore(new_gps, "my_collection", f"gps_{new_gps.gps_id}")


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
