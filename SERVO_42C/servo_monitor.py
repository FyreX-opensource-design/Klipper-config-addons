#imports
import pyserial
from servo_control import serial1
from servo_control import serial2

class monitor:
    def Xblocking():
        serial1.write('e0 3e 1e')
        output = serial1.read(8)
        result = output[3:5]
        if result == '02':
            return 'Xclear'
        elif result == '01':
            print("X stepper is blocked!")
            return 'Xblocked'
        elif result == '00':
            return 1
        else:
            return 11
    
    def Yblocking():
        serial2.write('e1 3e 1e')
        output = serial2.read(8)
        result = output[3:5]
        if result == '02':
            return 'Yclear'
        elif result == '01':
            print("Y stepper is blocked!")
            return 'Yblocked'
        elif result == '00':
            return 1
        else:
            return 11

if __name__ == __main__:
    monitor()
        