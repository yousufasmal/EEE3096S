#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: yousuf asmal
Student Number: ASMYOU001
Prac: 1
Date: 29/07/2019
"""





import RPi.GPIO as GPIO            #importing module for GPIO use
import time
GPIO.setmode(GPIO.BOARD)           #board pin numbering system

GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW) #initalizing pin as an output and setting is low
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(16, GPIO.IN)
GPIO.setup(12, GPIO.IN)


arrB =['000','001','010','011','100','101','110','111']
ind = 0                        #this will control where the index is pointing to which array slot
BNum='000'

def buttonUp(nothing):
    global ind
    global BNum
    arrB =['000','001','010','011','100','101','110','111']
    ind+=1
    if (ind==8):                        #if pass 7 go to 0
        ind=0
    BNum=arrB[ind] 
    print(ind)
    lightOn()
                                                         #if up button pushed

def buttonDown(nothing):
    global ind
    global BNum
    arrB =['000','001','010','011','100','101','110','111']
    ind-=1
    if(ind==-1):                           #if pass 0 go to 7
        ind=7
    BNum=arrB[ind]
    print(ind)
    lightOn()


    
def lightOn():
    global BNum
    print(BNum)
   # GPIO.output(11, GPIO.HIGH)
    if(BNum[0]=='0'):                   #sets what is in arrB at ind, each char in array element
        GPIO.output(11, GPIO.HIGH)
    else:
        GPIO.output(11, GPIO.LOW)
    
    if(BNum[1]=='0'):                   #sets what is in arrB at ind, each char in array element
        GPIO.output(13, GPIO.HIGH)
    else:
        GPIO.output(13, GPIO.LOW)
    
    if(BNum[2]=='0'):                   #sets what is in arrB at ind, each char in array element
        GPIO.output(15, GPIO.HIGH)
    else:
        GPIO.output(15, GPIO.LOW) 
    print("lighton")

def main():
    
   # GPIO.output(11, GPIO.HIGH)
   # GPIO.output(13, GPIO.HIGH)
   # GPIO.output(15, GPIO.HIGH)
    time.sleep(1)    
    
    GPIO.add_event_detect(16, GPIO.RISING, callback=buttonUp,bouncetime=300)        
    GPIO.add_event_detect(12, GPIO.RISING, callback=buttonDown,bouncetime=300) 
    
    while(True):
        time.sleep(0.0911)
    
# Only run the functions if
if __name__ == "__main__":
# Make sure the GPIO is stopped correctly

    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except:
        print("Some other error occurred")

GPIO.cleanup()