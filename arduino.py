import serial
import time

# here you choose your com
com = serial.Serial('COM7', baudrate = 9600, timeout=1)
points = 2
list = [0]*points
time.sleep(3)
# create input to get data
inp = input("getData  ").strip()
lastInput = 0;


while True:

    if inp != '':
        #writing to serial port
        com.write(inp.encode())
        time.sleep(0.5)
        # port echo
        data = com.readline().decode('ascii')
        print("sending data "+data)
        print("")
        # create input to get data
        inp = input("input data: ").strip()
