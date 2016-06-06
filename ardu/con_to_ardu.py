import serial
import statistics

PORT = 'com3'
SPEED = 9600

serial_connection = serial.Serial(PORT, SPEED)
while True:
    line = serial_connection.readline().decode()
    line_s = line.split(' ')
    form_number = line_s.pop()[:4]
    line_s = [int(x) for x in line_s]
    avr = statistics.mean(line_s)
    print("Для формы №:", form_number)
    print("Среднее натяжение:", avr)
    if form_number == '6666':
        break

serial_connection.close()
print("Работа окончена.")
