import sys
import os
import pygame
from random import randrange
from subprocess import Popen
from time import sleep
import RPi.GPIO as GPIO

a = 17
b = 18
c = 27
d = 22
e = 23
f = 24
g = 25

b1 = 19
b2 = 16
b3 = 26
b4 = 20

v1 = False
v2 = False
v3 = False
v4 = False
gameGo = False

#GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
#screen = pygame.display.set_mode(30,20)

GPIO.setup(a, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(b, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(c, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(d, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(e, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(f, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(g, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(b1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(b2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(b3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(b4, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    if GPIO.input(a) == False:
        os.system('sudo killall omxplayer.bin')
        os.system('omxplayer /home/pi/Videos/1.mov') 
    else:
        os.system('sudo killall omxplayer.bin')
    if GPIO.input(b) == False:
        os.system('sudo killall omxplayer.bin')
        os.system('omxplayer /home/pi/Videos/2.mov')
    if GPIO.input(c) == False:
        os.system('sudo killall omxplayer.bin')
        os.system('omxplayer /home/pi/Videos/3.mov')
    if GPIO.input(d) == False:
        os.system('sudo killall omxplayer.bin')
        os.system('omxplayer /home/pi/Videos/4.mov')
    if GPIO.input(e) == False:
        os.system('sudo killall omxplayer.bin')
        os.system('omxplayer /home/pi/Videos/5.mov')
    if GPIO.input(f) == False:
        os.system('sudo killall omxplayer.bin')
        os.system('omxplayer /home/pi/Videos/6.mov')
        
image1 = ('/home/pi/Videos/v1.jpg')

while True:
    pygame.init()

    width = pygame.display.Info().current_w
    height = pygame.display.Info().current_h
    
    screen = pygame.display.set_mode((width, height))

    difference = pygame.image.load(image1)
    difference = pygame.transform.scale(difference, (width, height))

    screen.blit(difference, (0, 0))
    pygame.display.update()

    inputValue1 = GPIO.input(16)
    inputValue2 = GPIO.input(20)
    inputValue3 = GPIO.input(26)
    inputValue4 = GPIO.input(19)
    if (inputValue1 == False):
        print("Button 16")
        image1 = ('/home/pi/Videos/v2.jpg')
    elif (inputValue3 == False):
        print("Button 20")
        image1 = ('/home/pi/Videos/v3.jpg')
    elif (inputValue4 == False):
        print("Button 26")
        image1 = ('/home/pi/Videos/v4.jpg')
