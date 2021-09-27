#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


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
robot = DriveBase(leftMotor, rightMotor, wheel_diameter=56, axle_track=114)
start = 0
# when pressed boolean program = true

while True:
    if(start == 0 and touch_avpa.pressed()):
        ev3.speaker.say("Exercise 2")
        while (start == 0):
            robot.drive(200, 0)
            if (ultra.distance() < 100):
                robot.stop()
                robot.straight(-70)
                robot.turn(80)
            if (touch_avpa.pressed()):
                start = 1
        if (start == 1 and touch_avpa.pressed()):
            robot.stop()
            ev3.speaker.say("Exercise 2 done")
            start = 0
