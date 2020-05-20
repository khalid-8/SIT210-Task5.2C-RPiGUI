from tkinter import *
import tkinter.font as tkFont
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT) 
GPIO.output(21, GPIO.LOW)
GPIO.setup(16, GPIO.OUT) 
GPIO.output(16, GPIO.LOW)
GPIO.setup(20, GPIO.OUT) 
GPIO.output(20, GPIO.LOW)

win = Tk()

myFont = tkFont.Font(family = 'Helvetica', size = 18, weight = 'bold')

def BlueON():
    print("button pressed")
    if GPIO.input(21) :
        GPIO.output(21,GPIO.LOW)
        BlueButton["text"] = "Blue ON"
    else:
        GPIO.output(21,GPIO.HIGH)
        BlueButton["text"] = "Blue OFF"

def GreenON():
    print("button pressed")
    if GPIO.input(20) :
        GPIO.output(20,GPIO.LOW)
        GreenButton["text"] = "Green ON"
    else:
        GPIO.output(20,GPIO.HIGH)
        GreenButton["text"] = "Green OFF"
                
def RedON():
    print("button pressed")
    if GPIO.input(16) :
        GPIO.output(16,GPIO.LOW)
        RedButton["text"] = "Red ON"
    else:
        GPIO.output(16,GPIO.HIGH)
        RedButton["text"] = "Red OFF"

def exitProgram():
    print("Exit Button pressed")
    GPIO.cleanup()
    win.quit()  


win.title("LED GUI")
win.geometry('500x300')



BlueButton = Button(win, text = "Blue", font = myFont, command = BlueON, height = 2, width =8)
BlueButton.pack(side = LEFT)

GreenButton = Button(win, text = "Green", font = myFont, command = GreenON, height = 2, width =8 )
GreenButton.pack(side = LEFT)

RedButton = Button(win, text = "Red", font = myFont, command = RedON, height = 2, width =8 )
RedButton.pack(side = LEFT)


mainloop()
