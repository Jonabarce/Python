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
ev3.screen.print("Hello World")
leftMotor = Motor(port=Port.B)
rightMotor = Motor(port=Port.C)

robot = DriveBase(leftMotor, rightMotor, wheel_diameter=56, axle_track=114)


for i in range(4):
    robot.straight(500)
    robot.stop()
    robot.turn(90)

ev3.speaker.say("Have a nice day")

