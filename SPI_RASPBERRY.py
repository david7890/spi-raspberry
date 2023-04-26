import spidev
import time
import RPi.GPIO as GPIO

# Crear un objeto spi
spi = spidev.SpiDev()
spi.open(0, 0) # Abrir el bus SPI 0, dispositivo 0
spi.max_speed_hz = 1000000 # Establecer la velocidad de la comunicación SPI

# Configurar el pin GPIO 8 como salida
GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.OUT)

# Bucle infinito para enviar datos continuamente
while True:
    # Enviar datos a través de SPI
    spi.xfer2([0x01, 0x02, 0x03]) # Aquí puedes ajustar los datos que deseas enviar
    
    # Imprimir mensaje en consola
    print("Datos enviados: [0x01, 0x02, 0x03]") # Aquí puedes ajustar el mensaje que deseas imprimir
    
    # Encender el pin GPIO 8 durante 1 segundo
    GPIO.output(8, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(8, GPIO.LOW)
    
    time.sleep(2) # Esperar 2 segundos