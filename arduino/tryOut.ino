#include <FirestoreESP8266.h>

Firestore fs;

void setup() {
  ...
  // Inicializar la conexión a WiFi
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("Conectado a WiFi");

  // Inicializar la conexión a Firestore
  fs.begin(FIREBASE_HOST, FIREBASE_AUTH_KEY);
}

// Función para leer datos de Firestore
void readData() {
  // Obtener el documento "acceso"
  DocumentReference doc = fs.collection("acceso").document("user_1");

  // Leer el valor del campo "acceso"
  bool acceso = doc.get().getBool("acceso");

  // Imprimir el valor leído
  Serial.println("Acceso concedido: " + (acceso ? "Sí" : "No"));
}

// Función para escribir datos en Firestore
void writeData() {
  // Crear un nuevo documento
  DocumentReference doc = fs.collection("acceso").document("user_2");

  // Escribir el valor "true" en el campo "acceso"
  doc.update({"acceso": true});
}
