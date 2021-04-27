from vpython import *
from time import *
import numpy as np
import math
import serial
ad=serial.Serial('/dev/ttyUSB0',2000000)
sleep(1)


scene.autoscale = False
scene.range=5
#scene.background=color.black
scene.autoscale = False
sp = sphere(pos=vector(0,0,0),texture="https://i.imgur.com/1nVWbbd.jpg",radius=25,shininess=0)
scene.forward=vector(-1,-1,-1)
toRad=2*np.pi/360
toDeg=1/toRad


scene.width=1200
scene.height=1080


bBoard=box(length=3,width=2,height=.2,pos=vector(0,0,0,))
sensor=box(length=.8,width=.75,height=.1, pos=vector(-.5,.1+.05,0),color=color.blue)
nano=box(lenght=1.75,width=.6,height=.1,pos=vector(1,.1+.05,0),color=color.green)
strap1=cylinder(length=0.3,radius=0.02,pos=vector(-0.1,0.1,0.8), axis=vector(1,0,0), color=color.red)
strap2=cylinder(length=0.3,radius=0.02,pos=vector(-0.1,0.1,-0.8), axis=vector(1,0,0), color=color.red)
strap3=cylinder(length=1.5,radius=0.02,pos=vector(-0.5,0.1,-0.4), axis=vector(1,0,0), color=color.green)                                                                              
strap4=cylinder(length=1.4,radius=0.02,pos=vector(-0.38,0.1,-0.45), axis=vector(1,0,0), color=color.yellow)
strap5=cylinder(length=0.35,radius=0.02,pos=vector(-0.5,0.1,-0.8), axis=vector(0,0,1), color=color.red)
strap6=cylinder(length=0.39,radius=0.02,pos=vector(-0.6,0.1,-0.9), axis=vector(0,0,1), color=color.black)
strap7=cylinder(length=0.35,radius=0.02,pos=vector(1.3,0.1,-0.8), axis=vector(0,0,1), color=color.red)
strap8=cylinder(length=0.39,radius=0.02,pos=vector(1.2,0.1,-0.9), axis=vector(0,0,1), color=color.black)
myObj=compound([bBoard,sensor,nano,strap1,strap2,strap3,strap4,strap5,strap6,strap7,strap8])

'''
bBoard=box(length=6,width=2,height=.2,opacity=.8,pos=vector(0,0,0,))
bn=box(length=1,width=.75,height=.1, pos=vector(-.5,.1+.05,0),color=color.blue)
nano=box(lenght=1.75,width=.6,height=.1,pos=vector(-2,.1+.05,0),color=color.green)
myObj=compound([bBoard,bn,nano])'''

r=vector(0,0,0)
graden = 0
t=0

while (True):
    try:
        while (ad.inWaiting()==0):
            pass
        dataPacket=ad.readline()
        dataPacket=str(dataPacket,'utf-8')
        splitPacket=dataPacket.split(",")
        q0=float(splitPacket[0])
        q1=float(splitPacket[1])
        q2=float(splitPacket[2])
        q3=float(splitPacket[3])

        roll=-math.atan2(2*(q0*q1+q2*q3),1-2*(q1*q1+q2*q2))
        pitch=math.asin(2*(q0*q2-q3*q1))
        yaw=-math.atan2(2*(q0*q3+q1*q2),1-2*(q2*q2+q3*q3))-np.pi/2

        rate(50)
        
        k=vector(cos(yaw)*cos(pitch), sin(pitch),sin(yaw)*cos(pitch))
        y=vector(0,1,0)
        s=cross(k,y)
        v=cross(s,k)
        vrot=v*cos(roll)+cross(k,v)*sin(roll)
       
        myObj.axis=-k
        myObj.up=vrot
        
        myObj.pos = -r
        r.x += 0.025
        
        sp.pos = -(4*vector(cos(t),0,sin(t)))
        t = q0*5
        #t += 0.025
        
    except:
        pass 