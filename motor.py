import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) 
   
class Engine(object):

    # constructor
    def __init__(self, engineA, engineB, engineE, name):
        self.name = name;
        self.speed = 0;
        self.turn = 0;
        self.engineA = engineA 
        self.engineB = engineB 
        self.engineE = engineE 
        GPIO.setup(self.engineA, GPIO.OUT)
        GPIO.setup(self.engineB, GPIO.OUT)
        GPIO.setup(self.engineE, GPIO.OUT)
        self.Engine = GPIO.PWM(self.engineE, 50)
        self.Engine.start(0)
    
    # stop engine
    def stop(self):
        # print "stop"
        self.speed = 0
        self.turn = 0
        self.setSpeed()
    
    # drive forward
    def forward(self, speed):
        # print "forward2"
        self.speed = speed
        GPIO.output(self.engineA, GPIO.HIGH)
        GPIO.output(self.engineB, GPIO.LOW)
        self.setSpeed()
    
    # drive backward
    def backward(self, speed):
        self.speed = speed
        GPIO.output(self.engineB, GPIO.HIGH)
        GPIO.output(self.engineA, GPIO.LOW)
        self.setSpeed()

    # turn
    def setTurn(self, turn):
        self.turn = turn
        self.setSpeed()

    # speed   
    def setSpeed(self):
        if (self.turn == 0):
            speed = self.speed
        else:
            speed = self.speed - int((self.speed * self.turn) / 100)
        self.Engine.ChangeDutyCycle(speed)
