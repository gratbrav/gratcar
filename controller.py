import os, sys, pygame, time
import RPi.GPIO as GPIO
from ConfigParser import ConfigParser
from car import Car
from pygame import locals

mycar = Car();
os.environ["SDL_VIDEODRIVER"] = "dummy"

config = ConfigParser()
config.sections()
config.read('config.ini')
        
maxSpeed = config.getint('Config', 'maxSpeed')
deadZone = 0.1

#find controller
count = 0
while (count == 0):
    try:
       pygame.init()
       pygame.joystick.init()
       j = pygame.joystick.Joystick(0)
       j.init() # init instance
       count = 1
    except pygame.error:
       pygame.quit()

try:
   j = pygame.joystick.Joystick(0)
   j.init()
   print 'Enabled joystick: ' + j.get_name()
except pygame.error:
   print 'no joystick found.'

speed = 0

try:
  while 1:
   for e in pygame.event.get(): # iterate over event stack
      if e.type == pygame.locals.JOYBUTTONDOWN:
         exit()
          
      if e.type == pygame.locals.JOYAXISMOTION: # Read Analog Joystick Axis
         x1 , y1 = j.get_axis(0), j.get_axis(1) # Left Stick
         y2 , x2 = j.get_axis(2), j.get_axis(3) # Right Stick

         if y2 < -1 * deadZone:
             speed = int((100 * y2) * -1)
             mycar.turnLeft(speed)

         if y2 > deadZone:
             speed = int((100 * y2))
             mycar.turnRight(speed)

         if y2 <= deadZone and y2 >= -1 * deadZone:
             mycar.turnRight(0)
             mycar.turnLeft(0)
             
         if y1 <= deadZone and y1 >= -1 * deadZone:
             mycar.stop()

         if y1 < -1 * deadZone:
             speed = int((maxSpeed * y1) * -1)
             mycar.forward(speed)

         if y1 > deadZone:
             speed = int((maxSpeed * y1))
             mycar.backward(speed)

finally:
    GPIO.cleanup()
    print "end"
