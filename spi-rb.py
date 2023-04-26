import spidev
import time
import RPi.GPIO as GPIO

# Crear un objeto spi
spi = spidev.SpiDev()
spi.open(0, 0) # Abrir el bus SPI 0, dispositivo 0
spi.max_speed_hz = 5000 # Establecemos velocidad maxima

# Configurar el pin GPIO 8 como salida
GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.OUT)

# Bucle infinito para enviar datos continuamente
while True:
    # Enviar bytes en hexadecimal a través de SPI
    spi.xfer([0x48, 0x4F, 0x4C, 0x41]) # Aquí puedes ajustar los datos que deseas enviar
    
    # Imprimir mensaje en consola
    print("Datos enviados: [H,O,L,A]")
    
    # Encender el pin GPIO 8
    GPIO.output(8, GPIO.HIGH)
    #time.sleep(1)
    #GPIO.output(8, GPIO.LOW)
    
    time.sleep(1) # Esperar 2 segundos
