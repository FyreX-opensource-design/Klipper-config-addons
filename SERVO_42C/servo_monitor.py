#imports 
import pyserial
import subprocess
from servo_control import serial1nj
from servo_control import serial2

def shutdown():
    subprocess.Popen('echo PRINTER_SHUTDOWN > /tmp/printer', shell=True)

class monitor:
    def Xblocking():
        serial1.write('e0 3e 1e')
        output = serial1.read(8)
        result = output[3:5]
        if result == '02':
            subprocess.Popen('echo M118 X stepper clear > /tmp/printer', shell=True)
        elif result == '01':
            subprocess.Popen('echo M118 X stepper blocked > /tmp/printer', shell=True)
            shutdown()
        elif result == '00':
            subprocess.Popen('echo M118 X stepper error > /tmp/printer', shell=True)
            shutdown()
        else:
            subprocess.Popen('echo M118 Unexplained error on X stepper > /tmp/printer', shell=True)
    
    def Yblocking():
        serial2.write('e1 3e 1e')
        output = serial2.read(8)
        result = output[3:5]
        if result == '02':
            subprocess.Popen('echo M118 Y stepper clear > /tmp/printer', shell=True)
        elif result == '01':
            subprocess.Popen('echo M118 Y stepper blocked > /tmp/printer', shell=True)
            shutdown()
        elif result == '00':
            subprocess.Popen('echo M118 Y stepper error > /tmp/printer', shell=True)
            shutdown()
        else:
            subprocess.Popen('echo M118 Unexplained error on Y stepper > /tmp/printer', shell=True)

if __name__ == "__main__":
    monitor()
        