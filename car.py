from ConfigParser import ConfigParser
from engine import Engine

class Car(object):

    # constructor
    def __init__(self):
        config = ConfigParser()
        config.sections()
        config.read('config.ini')
        self.engineLeft = Engine(config.getint('EngineLeft', 'A'), config.getint('EngineLeft', 'B'), config.getint('EngineLeft', 'E'), 'EngineLeft')
        self.engineRight = Engine(config.getint('EngineRight', 'A'), config.getint('EngineRight', 'B'), config.getint('EngineRight', 'E'), 'EngineRight')

    # stop engine
    def stop(self): 
        self.engineLeft.stop()
        self.engineRight.stop()

    # drive forward
    def forward(self, speed):
        self.engineLeft.forward(speed)
        self.engineRight.forward(speed)

    # drive backward
    def backward(self, speed):
        self.engineLeft.backward(speed)
        self.engineRight.backward(speed)

    # turn right
    def turnRight(self, turn):
        self.engineRight.setTurn(turn)
    
    # turn left
    def turnLeft(self, turn):
        self.engineLeft.setTurn(turn)
        