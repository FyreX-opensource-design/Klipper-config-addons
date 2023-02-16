#imports
import pyserial
import time

serial1 = serial.Serial('/dev/ttyUSB0') #x stepper
serial2 = serial.Serial('/dev/ttyUSB1') #y stepper

#sends calabrate command
def calabrate():
    if stepper1 == 'X':
        serial1.write('e0 80 00 60')
    elif stepper1 == 'Y'
        serial1.write('e1 80 00 60')
    else:
        return 10
    time.sleep(60)
    #reads success or fail output
    output = serial1.read(8)
    result = output[3:5]
    if result == '01':
        return 0
    elif result == '00':
        return 1
    else:
        return 11
#main body
if __name__ == '__main__':
    if command == 'cal':
        calabrate()
