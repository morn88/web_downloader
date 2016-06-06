import serial
import statistics
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
fig = plt.figure()

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
    ys = line_s
    xs = [x for x in range(len(line_s))]
    plt.plot(xs, ys)
    plt.title("Form number: " + form_number)
    plt.show()
    if form_number == '6666':
        break

serial_connection.close()
print("Работа окончена.")
