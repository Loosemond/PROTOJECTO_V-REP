# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 17:51:35 2017

@author: João Ribeiro
"""

import vrep
import sys
import time # ATENÇAO NAO SE PODE ACELARAR O TEMPO NO VREP POIS ASSIM PERDE O SINC ARRANJAR UMA MANEIRA DE OBTER O TEMPO APARTIR O V-REP
import math

Vdireita=1
Vesquerda=1
done=False
skip=False
evade=False
vrep.simxFinish(-1) # just in case, close all opened connections
clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to V-REP
if clientID!=-1:
    print ('Connected to remote API server')
    
else:
    print ('Nao foi possivel conectar ')
    sys.exit('erro_1') #sai do programa 
    
errorCode,left_motor_handle=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_leftMotor',vrep.simx_opmode_oneshot_wait) # define os motores dando lhes um nome novo pois os motores ja tem um nome que lhes foi atribuido no v-rep
errorCode,right_motor_handle=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_rightMotor',vrep.simx_opmode_oneshot_wait)


errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,Vesquerda,vrep.simx_opmode_streaming) # define uma velucidade a uma dada roda

errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,Vdireita,vrep.simx_opmode_streaming) #o error code serve para saber se ta tudo a funcionar direito caso a var error code =! de 0 algo ta mal
#define os sensores ultrasonicos
errorCode,sensor1=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor1',vrep.simx_opmode_oneshot_wait) #define os sensores ultrasonicos E
errorCode,sensor4=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor4',vrep.simx_opmode_oneshot_wait) #define os sensores ultrasonicos
errorCode,sensor5=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor5',vrep.simx_opmode_oneshot_wait) #define os sensores ultrasonicos
errorCode,sensor8=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor8',vrep.simx_opmode_oneshot_wait) #define os sensores ultrasonicos D
errorCode,sensor9=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor9',vrep.simx_opmode_oneshot_wait) #define os sensores ultrasonicos D
errorCode,sensor16=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor16',vrep.simx_opmode_oneshot_wait) #define os sensores ultrasonicos E
#inicia os sensores 
errorCode,detectionState1,detectedPoint1,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor1,vrep.simx_opmode_streaming) # 1 E F
errorCode,detectionState4,detectedPoint4,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor4,vrep.simx_opmode_streaming) # 4
errorCode,detectionState5,detectedPoint5,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor5,vrep.simx_opmode_streaming) # 5
errorCode,detectionState8,detectedPoint8,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor8,vrep.simx_opmode_streaming) # 8 D F
errorCode,detectionState9,detectedPoint9,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor9,vrep.simx_opmode_streaming) # 9 D T
errorCode,detectionState16,detectedPoint16,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor16,vrep.simx_opmode_streaming) # 16 E T

evadeETime=time.time()
evadeDTime=time.time()
startTime=time.time()
while time.time()-startTime < 120 : #loop
    time.sleep(0.2)
    skip=False
    errorCode,detectionState1,detectedPoint1,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor1,vrep.simx_opmode_buffer)
    errorCode,detectionState4,detectedPoint4,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor4,vrep.simx_opmode_buffer)
    errorCode,detectionState5,detectedPoint5,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor5,vrep.simx_opmode_buffer)
    errorCode,detectionState8,detectedPoint8,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor8,vrep.simx_opmode_buffer)
    errorCode,detectionState9,detectedPoint9,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor9,vrep.simx_opmode_buffer)
    errorCode,detectionState16,detectedPoint16,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor16,vrep.simx_opmode_buffer)

   # time.sleep(0.01)
    
    #print(math.sqrt(detectedPoint1[0]**2+detectedPoint1[1]**2+detectedPoint1[2]**2))
    detectedPoint1=math.sqrt(detectedPoint1[0]**2+detectedPoint1[1]**2+detectedPoint1[2]**2)
    detectedPoint4=math.sqrt(detectedPoint4[0]**2+detectedPoint4[1]**2+detectedPoint4[2]**2)
    detectedPoint5=math.sqrt(detectedPoint5[0]**2+detectedPoint5[1]**2+detectedPoint5[2]**2)
    detectedPoint8=math.sqrt(detectedPoint8[0]**2+detectedPoint8[1]**2+detectedPoint8[2]**2)
    detectedPoint9=math.sqrt(detectedPoint9[0]**2+detectedPoint9[1]**2+detectedPoint9[2]**2)
    detectedPoint16=math.sqrt(detectedPoint16[0]**2+detectedPoint16[1]**2+detectedPoint16[2]**2)
    print(detectedPoint1,detectedPoint16)
    #print('4',detectionState4)
    #print('8',detectionState8)#teste para verificar se ta a detetar alguma coisa com o sensor
    if detectedPoint4 < 0.01 and detectedPoint5 < 0.01:
        done = False
        if detectionState1 == False and done == False:
           Vdireita = 0
           Vesquerda = 1
           errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,Vdireita,vrep.simx_opmode_streaming)
           errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,Vesquerda,vrep.simx_opmode_streaming)
           time.sleep(1.5) # vai depender da velucidade e do atrito do robo !!!
           Vdireita = 1
           Vesquerda = 1
           errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,Vdireita,vrep.simx_opmode_streaming)
           errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,Vesquerda,vrep.simx_opmode_streaming)
           #time.sleep(1) # refers is to fast!!! assim evita que o robo ande as voltas 
           done = True
        if detectionState8 == False and done == False:
           Vdireita = 1
           Vesquerda = 0
           errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,Vdireita,vrep.simx_opmode_streaming)
           errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,Vesquerda,vrep.simx_opmode_streaming)
           time.sleep(1.5) # vai depender da velucidade e do atrito do robo !!!
           Vdireita = 1
           Vesquerda = 1
           errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,Vdireita,vrep.simx_opmode_streaming)
           errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,Vesquerda,vrep.simx_opmode_streaming)
          # time.sleep(1)
           done = True
        if detectionState8 == True and done == False and detectionState1 == True:
           Vdireita = -0.5
           Vesquerda = 0.5
           errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,Vdireita,vrep.simx_opmode_streaming)
           errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,Vesquerda,vrep.simx_opmode_streaming)
           time.sleep(3.25)
           Vdireita = 1
           Vesquerda = 1
           errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,Vdireita,vrep.simx_opmode_streaming)
           errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,Vesquerda,vrep.simx_opmode_streaming)
    if detectionState1==True and detectionState16==True  :
        skip=True 
        Pesquerda=abs(detectedPoint1 - detectedPoint16)     
        if  Pesquerda > 0.01 : #evita que raspe na parede 
            if detectedPoint1 > detectedPoint16:
                Vdireita = 0
                Vesquerda = 1
                errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,Vdireita,vrep.simx_opmode_streaming)
                errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,Vesquerda,vrep.simx_opmode_streaming)
                if Pesquerda > 0.15  :
                    time.sleep(0.6)
                   
                        
                time.sleep(0.1)
                Vdireita = 1
                Vesquerda = 1
                errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,Vdireita,vrep.simx_opmode_streaming)
                errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,Vesquerda,vrep.simx_opmode_streaming)
            else:
                Vdireita = 1
                Vesquerda = 0
                errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,Vdireita,vrep.simx_opmode_streaming)
                errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,Vesquerda,vrep.simx_opmode_streaming)
                if Pesquerda > 0.15 :
                    time.sleep(0.6)
                time.sleep(0.1)
                Vdireita = 1
                Vesquerda = 1
                errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,Vdireita,vrep.simx_opmode_streaming)
                errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,Vesquerda,vrep.simx_opmode_streaming)
    if detectionState8==True and detectionState9==True and skip==False :
         Pdireita= abs(detectedPoint8 - detectedPoint9)
         if detectedPoint8 - detectedPoint9 > 0.01 or detectedPoint8 - detectedPoint9 < -0.01  : #evita que raspe na parede 
            if detectedPoint8 > detectedPoint9:
                Vdireita = 1
                Vesquerda = 0
                errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,Vdireita,vrep.simx_opmode_streaming)
                errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,Vesquerda,vrep.simx_opmode_streaming)
                if Pdireita > 0.15  :
                    time.sleep(0.6)
                   
                time.sleep(0.1)
                Vdireita = 1
                Vesquerda = 1
                errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,Vdireita,vrep.simx_opmode_streaming)
                errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,Vesquerda,vrep.simx_opmode_streaming)
            else:
                Vdireita = 0
                Vesquerda = 1
                errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,Vdireita,vrep.simx_opmode_streaming)
                errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,Vesquerda,vrep.simx_opmode_streaming)
                if Pdireita > 0.15  :
                    time.sleep(0.6)
                time.sleep(0.1)
                Vdireita = 1
                Vesquerda = 1
                errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,Vdireita,vrep.simx_opmode_streaming)
                errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,Vesquerda,vrep.simx_opmode_streaming)