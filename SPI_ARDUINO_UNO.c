#include <SPI.h>

// Definir pines para la comunicación SPI en el Arduino Uno
#define SS_PIN 10
#define MOSI_PIN 11
#define MISO_PIN 12
#define SCK_PIN 13

void setup() {
  Serial.begin(9600); // Inicializar la comunicación serial para imprimir mensajes en el monitor serial
  SPI.begin(); // Inicializar la comunicación SPI
  pinMode(SS_PIN, INPUT); // Configurar el pin SS como entrada para actuar en modo esclavo
}

void loop() {
  if (digitalRead(SS_PIN) == LOW) { // Verificar si el pin SS está activo (en bajo)
    byte data_received = SPI.transfer(0x00); // Leer datos recibidos a través del bus SPI
    Serial.print("Dato recibido: ");
    Serial.println(data_received, HEX); // Imprimir el dato recibido en hexadecimal
  }
}