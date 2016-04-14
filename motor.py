import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) 
   
class Motor(object):

    # constructor
    def __init__(self, motorA, motorB, motorE, name):
        self.name = name;
        self.speed = 0;
        self.turn = 0;
        self.motorA = motorA 
        self.motorB = motorB 
        self.motorE = motorE 
        GPIO.setup(self.motorA, GPIO.OUT)
        GPIO.setup(self.motorB, GPIO.OUT)
        GPIO.setup(self.motorE, GPIO.OUT)
        self.Motor = GPIO.PWM(self.motorE, 50)
        self.Motor.start(0)
    
    # stop motor
    def stop(self):
        # print "stop"
        self.speed = 0
        self.turn = 0
        self.setSpeed()
    
    # drive forward
    def forward(self, speed):
        # print "forward2"
        self.speed = speed
        GPIO.output(self.motorA, GPIO.HIGH)
        GPIO.output(self.motorB, GPIO.LOW)
        self.setSpeed()
    
    # drive backward
    def backward(self, speed):
        self.speed = speed
        GPIO.output(self.motorB, GPIO.HIGH)
        GPIO.output(self.motorA, GPIO.LOW)
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
        self.Motor.ChangeDutyCycle(speed)
