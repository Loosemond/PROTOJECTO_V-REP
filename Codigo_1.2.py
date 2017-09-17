# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 17:51:35 2017

@author: João Ribeiro
"""

import vrep
import sys
import time # ATENÇAO NAO SE PODE ACELARAR O TEMPO NO VREP POIS ASSIM PERDE O SINC ARRANJAR UMA MANEIRA DE OBTER O TEMPO APARTIR O V-REP
import math

Vdireita=0
Vesquerda=0
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
#%% iniciaçao

def Sensores_ini(clientID):
    errorCode,left_motor_handle=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_leftMotor',vrep.simx_opmode_oneshot_wait) # define os motores dando lhes um nome novo pois os motores ja tem um nome que lhes foi atribuido no v-rep
    errorCode,right_motor_handle=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_rightMotor',vrep.simx_opmode_oneshot_wait)
    #define os sensores ultrasonicos
    errorCode,sensor1=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor1',vrep.simx_opmode_oneshot_wait) #define os sensores ultrasonicos E
    errorCode,sensor2=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor2',vrep.simx_opmode_oneshot_wait) #define os sensores ultrasonicos E
    errorCode,sensor4=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor4',vrep.simx_opmode_oneshot_wait) #define os sensores ultrasonicos
    errorCode,sensor5=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor5',vrep.simx_opmode_oneshot_wait) #define os sensores ultrasonicos
    errorCode,sensor7=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor7',vrep.simx_opmode_oneshot_wait) #define os sensores ultrasonicos E
    errorCode,sensor8=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor8',vrep.simx_opmode_oneshot_wait) #define os sensores ultrasonicos D
    errorCode,sensor9=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor9',vrep.simx_opmode_oneshot_wait) #define os sensores ultrasonicos D
    errorCode,sensor16=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor16',vrep.simx_opmode_oneshot_wait) #define os sensores ultrasonicos E
    return sensor1,sensor2,sensor4,sensor5,sensor7,sensor8,sensor9,sensor16

def Sensores_start(clientID,sensor1,sensor2,sensor4,sensor5,sensor7,sensor8,sensor9,sensor16): # inicia os sensores
   #inicia os sensores 
    errorCode,detectionState1,detectedPoint1,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor1,vrep.simx_opmode_streaming) # 1 E F
    errorCode,detectionState2,detectedPoint2,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor2,vrep.simx_opmode_streaming) # 1 E F curva 1º
    errorCode,detectionState4,detectedPoint4,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor4,vrep.simx_opmode_streaming) # 4
    errorCode,detectionState5,detectedPoint5,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor5,vrep.simx_opmode_streaming) # 5
    errorCode,detectionState7,detectedPoint7,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor7,vrep.simx_opmode_streaming) # 7 D F curva 1º
    errorCode,detectionState8,detectedPoint8,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor8,vrep.simx_opmode_streaming) # 8 D F
    errorCode,detectionState9,detectedPoint9,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor9,vrep.simx_opmode_streaming) # 9 D T
    errorCode,detectionState16,detectedPoint16,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor16,vrep.simx_opmode_streaming) # 16 E T
    return detectionState1,detectedPoint1,detectionState2,detectedPoint2,detectionState4,detectedPoint4,detectionState5,detectedPoint5,detectionState7,detectedPoint7,detectionState8,detectedPoint8,detectionState9,detectedPoint9,detectionState16,detectedPoint16

sensor1,sensor2,sensor4,sensor5,sensor7,sensor8,sensor9,sensor16=Sensores_ini(clientID)
detectionState1,detectedPoint1,detectionState2,detectedPoint2,detectionState4,detectedPoint4,detectionState5,detectedPoint5,detectionState7,detectedPoint7,detectionState8,detectedPoint8,detectionState9,detectedPoint9,detectionState16,detectedPoint16=Sensores_start(clientID,sensor1,sensor2,sensor4,sensor5,sensor7,sensor8,sensor9,sensor16)

errorCode,left_motor_handle=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_leftMotor',vrep.simx_opmode_oneshot_wait) # define os motores dando lhes um nome novo pois os motores ja tem um nome que lhes foi atribuido no v-rep
errorCode,right_motor_handle=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_rightMotor',vrep.simx_opmode_oneshot_wait)
#define os sensores ultrasonicos
errorCode,sensor1=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor1',vrep.simx_opmode_oneshot_wait) #define os sensores ultrasonicos E
errorCode,sensor2=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor2',vrep.simx_opmode_oneshot_wait) #define os sensores ultrasonicos E
errorCode,sensor4=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor4',vrep.simx_opmode_oneshot_wait) #define os sensores ultrasonicos
errorCode,sensor5=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor5',vrep.simx_opmode_oneshot_wait) #define os sensores ultrasonicos
errorCode,sensor7=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor7',vrep.simx_opmode_oneshot_wait) #define os sensores ultrasonicos E
errorCode,sensor8=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor8',vrep.simx_opmode_oneshot_wait) #define os sensores ultrasonicos D
errorCode,sensor9=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor9',vrep.simx_opmode_oneshot_wait) #define os sensores ultrasonicos D
errorCode,sensor16=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor16',vrep.simx_opmode_oneshot_wait) #define os sensores ultrasonicos E
#inicia os sensores 
errorCode,detectionState1,detectedPoint1,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor1,vrep.simx_opmode_streaming) # 1 E F
errorCode,detectionState2,detectedPoint2,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor2,vrep.simx_opmode_streaming) # 1 E F curva 1º
errorCode,detectionState4,detectedPoint4,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor4,vrep.simx_opmode_streaming) # 4
errorCode,detectionState5,detectedPoint5,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor5,vrep.simx_opmode_streaming) # 5
errorCode,detectionState7,detectedPoint7,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor7,vrep.simx_opmode_streaming) # 7 D F curva 1º
errorCode,detectionState8,detectedPoint8,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor8,vrep.simx_opmode_streaming) # 8 D F
errorCode,detectionState9,detectedPoint9,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor9,vrep.simx_opmode_streaming) # 9 D T
errorCode,detectionState16,detectedPoint16,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor16,vrep.simx_opmode_streaming)        



#errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,Vesquerda,vrep.simx_opmode_streaming) # define uma velucidade a uma dada roda
#
#errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,Vdireita,vrep.simx_opmode_streaming) #o error code serve para saber se ta tudo a funcionar direito caso a var error code =! de 0 algo ta mal
Vdireita=1
Vesquerda=1
errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,Vesquerda,vrep.simx_opmode_streaming)
errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,Vdireita,vrep.simx_opmode_streaming)
evadeETime=time.time()
evadeDTime=time.time()
startTime=time.time()
while time.time()-startTime < 120 : #loop
    time.sleep(0.05)
    skip=False
    errorCode,detectionState1,detectedPoint1,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor1,vrep.simx_opmode_buffer)
    errorCode,detectionState2,detectedPoint2,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor2,vrep.simx_opmode_buffer)
    errorCode,detectionState4,detectedPoint4,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor4,vrep.simx_opmode_buffer)
    errorCode,detectionState5,detectedPoint5,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor5,vrep.simx_opmode_buffer)
    errorCode,detectionState7,detectedPoint7,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor7,vrep.simx_opmode_buffer)
    errorCode,detectionState8,detectedPoint8,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor8,vrep.simx_opmode_buffer)
    errorCode,detectionState9,detectedPoint9,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor9,vrep.simx_opmode_buffer)
    errorCode,detectionState16,detectedPoint16,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sensor16,vrep.simx_opmode_buffer)
   
   # time.sleep(0.01)
    
    #print(math.sqrt(detectedPoint1[0]**2+detectedPoint1[1]**2+detectedPoint1[2]**2))
    detectedPoint1=math.sqrt(detectedPoint1[0]**2+detectedPoint1[1]**2+detectedPoint1[2]**2)
    detectedPoint2=math.sqrt(detectedPoint2[0]**2+detectedPoint2[1]**2+detectedPoint2[2]**2)
    detectedPoint4=math.sqrt(detectedPoint4[0]**2+detectedPoint4[1]**2+detectedPoint4[2]**2)
    detectedPoint5=math.sqrt(detectedPoint5[0]**2+detectedPoint5[1]**2+detectedPoint5[2]**2)
    detectedPoint7=math.sqrt(detectedPoint7[0]**2+detectedPoint7[1]**2+detectedPoint7[2]**2)
    detectedPoint8=math.sqrt(detectedPoint8[0]**2+detectedPoint8[1]**2+detectedPoint8[2]**2)
    detectedPoint9=math.sqrt(detectedPoint9[0]**2+detectedPoint9[1]**2+detectedPoint9[2]**2)
    detectedPoint16=math.sqrt(detectedPoint16[0]**2+detectedPoint16[1]**2+detectedPoint16[2]**2)
   
    #print('4',detectionState4)
    #print('8',detectionState8)#teste para verificar se ta a detetar alguma coisa com o sensor
    if detectedPoint4 < 0.01 and detectedPoint5 < 0.01:
        done = True
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
   
    if detectionState1==True and detectionState2==True  :
        skip=True 
        C_detectedPoint2=math.sin(math.sqrt(3)/2-math.pi/180)*detectedPoint2 # calcula a que distancia ta o objecto do robo em relaçao ao seu lado esquerdo
        print(detectedPoint1,C_detectedPoint2,detectedPoint2)
        Pesquerda=abs(detectedPoint1 - C_detectedPoint2)     
        if  Pesquerda > 0.01 : #evita que raspe na parede 
            if detectedPoint1 < C_detectedPoint2:
                Vdireita = 0
                Vesquerda = 1
                errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,Vdireita,vrep.simx_opmode_streaming)
                errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,Vesquerda,vrep.simx_opmode_streaming)
                if Pesquerda > 0.15  :
                    time.sleep(0.1)
                   
                        
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
                    time.sleep(0.1)
                time.sleep(0.1)
                Vdireita = 1
                Vesquerda = 1
                errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,Vdireita,vrep.simx_opmode_streaming)
                errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,Vesquerda,vrep.simx_opmode_streaming)
                
    if detectionState1==True and detectionState16==True and skip==False :
        skip=True 
        
        
        Pesquerda=abs(detectedPoint1 - detectedPoint16)     
        if  Pesquerda > 0.01 : #evita que raspe na parede 
            if detectedPoint1 > detectedPoint16:
                Vdireita = 0
                Vesquerda = 1
                errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,Vdireita,vrep.simx_opmode_streaming)
                errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,Vesquerda,vrep.simx_opmode_streaming)
                if Pesquerda > 0.15  :
                    time.sleep(0.1)
                   
                        
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
                    time.sleep(0.1)
                time.sleep(0.1)
                Vdireita = 1
                Vesquerda = 1
                errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,Vdireita,vrep.simx_opmode_streaming)
                errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,Vesquerda,vrep.simx_opmode_streaming)
    if detectionState8==True and detectionState7==True and skip==False : # direita superior 
         C_detectedPoint7=math.sin(math.sqrt(3)/2-math.pi/180)*detectedPoint7
         Pdireita= abs(detectedPoint8 - C_detectedPoint7)
         if Pdireita > 0.01 : #evita que raspe na parede 
            if detectedPoint8 < C_detectedPoint7:
                Vdireita = 1
                Vesquerda = 0
                errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,Vdireita,vrep.simx_opmode_streaming)
                errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,Vesquerda,vrep.simx_opmode_streaming)
                if Pdireita > 0.15  :
                    time.sleep(0.1)
                   
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
                    time.sleep(0.1)
                time.sleep(0.1)
                Vdireita = 1
                Vesquerda = 1
                errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,Vdireita,vrep.simx_opmode_streaming)
                errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,Vesquerda,vrep.simx_opmode_streaming)
                
    if detectionState8==True and detectionState9==True and skip==False : # e possivel que o sensor na diagonal nao apanhe nada assim temos a certesa qeu o robo esta sempre paralelo a parede
        skip=True  #direita inferior
        
        
        Pesquerda=abs(detectedPoint8 - detectedPoint9)     
        if  Pesquerda > 0.01 : #evita que raspe na parede 
            if detectedPoint8 < detectedPoint9:
                Vdireita = 0
                Vesquerda = 1
                errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,Vdireita,vrep.simx_opmode_streaming)
                errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,Vesquerda,vrep.simx_opmode_streaming)
                if Pesquerda > 0.15  :
                    time.sleep(0.1)
                   
                        
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
                    time.sleep(0.1)
                time.sleep(0.1)
                Vdireita = 1
                Vesquerda = 1
                errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,Vdireita,vrep.simx_opmode_streaming)
                errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,Vesquerda,vrep.simx_opmode_streaming)