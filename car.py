from ConfigParser import ConfigParser
from motor import Motor

class Car(object):

    # constructor
    def __init__(self):
        config = ConfigParser()
        config.sections()
        config.read('config.ini')
        self.motorLeft = Motor(config.getint('MotorLeft', 'A'), config.getint('MotorLeft', 'B'), config.getint('MotorLeft', 'E'), 'MotorLeft')
        self.motorRight = Motor(config.getint('MotorRight', 'A'), config.getint('MotorRight', 'B'), config.getint('MotorRight', 'E'), 'MotorRight')

    # stop motor
    def stop(self): 
        self.motorLeft.stop()
        self.motorRight.stop()

    # drive forward
    def forward(self, speed):
        self.motorLeft.forward(speed)
        self.motorRight.forward(speed)

    # drive backward
    def backward(self, speed):
        self.motorLeft.backward(speed)
        self.motorRight.backward(speed)

    # turn right
    def turnRight(self, turn):
        self.motorRight.setTurn(turn)
    
    # turn left
    def turnLeft(self, turn):
        self.motorLeft.setTurn(turn)
        