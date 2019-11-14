'''
Created on Jul 24, 2019

@author: daniel
'''
import serial

class Reader(object):
    '''
    This class is responsible for reading arduino's serial output 
    remember to del it in order for the connection to close
    '''
    ser = serial.Serial('/dev/ttyACM0')
    
    def lastRead(self):
        b = self.ser.readline() #this waits for the next input and no code will execute untill it gets one
        return int(b)
    def __init__(self):
        pass
        
    def __del__(self):
        self.ser.close()
        

