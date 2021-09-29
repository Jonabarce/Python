#!/usr/bin/env pybricks-micropython
import random
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import random


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()





# Write your program here.
ev3.speaker.beep()
leftMotor = Motor(port=Port.B)
rightMotor = Motor(port=Port.C)
ultra = UltrasonicSensor(port=Port.S2)
touch_avpa = TouchSensor(port=Port.S1)
Color_sensorMidten = ColorSensor(Port.S3)
Color_sensorHoyre = ColorSensor(Port.S4)
robot = DriveBase(leftMotor, rightMotor, wheel_diameter=56, axle_track=114)
total_run_time = 5000 #Tid før robot skal stoppe å underholde [ms]
interval = 500 #Interval for å oppdatere sensor data [ms]

def play_joke1():
    ev3.speaker.play_file(SoundFile.CHEERING)
    robot.turn(360)

def play_joke2():
    robot.turn(720)
    ev3.screen.print(" Fuck this shit im out ")

def play_joke3():
    ev3.speaker.say(" They see me rollin', they hatin' ")

def play_joke4():
    ev3.speaker.say(" Elo, this is me, stephen talking")

def perform_activity():

    if stop:
        ev3.speaker.play_file(SoundFile.FANFARE)
    else:
        r = random.randint(1, 4)
        if r == 1:
            play_joke1()
        elif r == 2:
            play_joke2()
        elif r == 3:
            play_joke3()
        elif r == 4:
            play_joke4()


stop = False

#Mens roboten ikke har signal om å stoppe
while not stop:
    for i in range(0, total_run_time / interval):
        distance = ultra.distance()
        reflectionMidten = Color_sensorMidten.reflection()
        reflectionHoyre = Color_sensorHoyre.reflection()

        ev3.screen.clear()
        ev3.screen.print("Distance: %s\nReflectionMidt: %s\nReflectionHoy %s" % (distance, reflectionMidten, reflectionHoyre))

        if distance <= 70:
            stop = True
            break

        while Color_sensorHoyre.reflection() < 15:
            Color_sensorHoyre.reflection()
            robot.turn(10)

        while Color_sensorMidten.reflection() > 12:
            Color_sensorMidten.reflection()
            robot.turn(-3)

        robot.drive(100, 0)
        wait(interval)
        robot.stop()

    #Hver gang totale kjøre tiden er ferdig, fremfør et show
    #Hvis stop er true, spill Fanfare
    perform_activity()