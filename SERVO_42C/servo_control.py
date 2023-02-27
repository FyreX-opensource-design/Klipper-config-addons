#imports
import pyserial
import time
global output

serial1 = serial.Serial('/dev/ttyUSB0', 9600) #x stepper
serial2 = serial.Serial('/dev/ttyUSB1', 9600) #y stepper

#reads success or fail output
def _return():
    result = output[3:5]
    if result == '01':
        return 0
    elif result == '00':
        return 1
    else:
        return 11

#sends calabrate command
def calabrate():
    if stepper1 == 'X':
        serial1.write('e0 80 00 60')
        time.sleep(60)
        output = serial1.read(8)
    elif stepper1 == 'Y':
        serial2.write('e1 80 00 60')
        time.sleep(60)
        output = serial2.read(8)
    else:
        return 10
    _return()

#sets work mode
def work_mode(mode):
    #sends open commands
    if mode == 'open':
        if stepper1 == 'X':
            serial1.write('e0 82 00 63')
            time.sleep(1)
            output = serial1.read(8)
        elif stepper1 == "Y":
            serial2.write('e1 82 00 63')
            time.sleep(1)
            output = serial2.read(8)
        else:
            return 10
    #sends close commands
    elif mode == 'closed':
        if stepper1 == 'X':
            serial1.write('e0 82 01 63')
            time.sleep(1)
            output = serial1.read(8)
        elif stepper1 == 'Y':
            serial2.write('e1 82 01 63')
            time.sleep(1)
            output = serial2.read(8)
        else:
            return 10
    else:
        return 10
    _return()
            
#main body
if __name__ == '__main__':
    if command == 'cal':
        calabrate()
    elif command == 'work':
        work_mode()
