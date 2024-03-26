#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Image


class Feladatok():

    def __init__(self):
        # tégla
        self.ev3 = EV3Brick()
        # motorok
        self.jm = Motor(Port.B)
        self.bm = Motor(Port.C)
        self.km = Motor(Port.A)
        # szenzorok
        self.cs = ColorSensor(Port.S3)
        self.ts = TouchSensor(Port.S1)
        self.gs = GyroSensor(Port.S2)
        self.us = UltrasonicSensor(Port.S4)
        #self.ir = InfraredSensor(Port.S4)

        # dupla motorkezelő
        self.robot = DriveBase(self.jm, self.bm, 55, 115)

        #stopper óra
        self.ido = StopWatch()
    
    def csipog(self):
        self.ev3.speaker.beep()

    
    def scanner(self):
        #Fényviszonyok:
        #feketevonal: 9
        #szürke asztal: 55
        #asztalról le : 0
        #félig az asztalról le: 22
        self.robot.drive(100,0)
        hol = 0
        self.ido.reset()
        while self.ido.time() < 3000:
            if self.cs.reflection() <(55+9)/2:
                self.ev3.screen.draw_line(hol,0,hol,127)
            hol += 1
            wait(3000/178)
        self.robot.stop(Stop.BRAKE)
        wait(10000)
    
    def harmadik(self):
        while self.cs.reflection() > (55+9)/2-18:
            self.robot.drive(100,0)
        self.robot.stop(Stop.BRAKE)
        while self.cs.reflection() > (55+9)/2-9:
            self.robot.drive(100,0)
        self.robot.stop(Stop.BRAKE)

    def hanyvonal(self, db, seb, hatar):
        for vonalakszama in range(db):
            vege = False
            feket = False
            self.robot.drive(seb,0)
            while not vege:
                if self.cs.reflection() < hatar:
                    fekete = True
                if fekete and self.cs.reflection() > hatar+9:
                    vege = True
        self.robot.stop(Stop.BRAKE)


    def elsob(self):
        hatar = (55+9)/2-10
        self.hanyvonal(5, 100,hatar)


    def elsoc(self):
        hatar = (55+9)/2-10
        self.hanyvonal(5, -100,hatar)

    def elsod(self):
        hosszok = []
        self.robot.drive(100,0)
        for vonalakszama in range (3)
            vege = False
            fekete = False
            self.robot.drive(100,0)
            while not vege:
                if self.cs.reflection() > (55+9)/2-18:
                    fekete = True
                    self.ido.reset()
                if self.cs.reflection() > (55+9)/2-9:
                    vege = True
                    hossz = self.ido.time()
                    hosszok.append(hossz)
            self.robot.stop(Stop.BRAKE)
            print(hossz)
        print(hosszok)