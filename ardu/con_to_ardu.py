import serial

PORT = 'com3'
SPEED = 9600

serial_connection = serial.Serial(PORT, SPEED)
for i in range(100):
    print(serial_connection.readline())

serial_connection.close()
