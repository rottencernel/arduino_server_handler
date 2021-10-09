import serial
import time

ser = serial.Serial('COM3', 9600, timeout=0)
data = []


def accept_com_port_message():
    mess = ser.readline()
    data.append(mess)
    time.sleep(1)


while ser:
    try:
        accept_com_port_message()
        with open("data.txt", "w") as file:
            file.write(str(data))
        print(data)
    except:
        print('Data could not be read')
        time.sleep(1)
        ser.close()


