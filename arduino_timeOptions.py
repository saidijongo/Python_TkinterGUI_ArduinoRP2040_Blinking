import serial
from tkinter import *
import tkinter as tk
import time

# Replace '/dev/ttyACM0' with the correct serial port of your Arduino
arduino_port = '/dev/ttyACM0'
baud_rate = 9600

# Open the serial connection
ser = serial.Serial(arduino_port, baud_rate, timeout=1)

def turnOnLED():
    if blinkState.get() == 1:
        blinkLED()
    else:
        ser.write(b'turn on')
        
def turnOffLED(): 
    ser.write(b'turn off')

def blinkLED():
    if blinkState.get() == 1:
        ser.write(b'blinking')
        time.sleep(1)
        delay = userDelay.get()
        ser.write(delay.encode())
        
# creating tkinter window 
root = Tk() 
root.title(' ArduinoLED Blink GUI')
root.configure(bg="red")

btn_On = tk.Button(root, text="Turn On", command=turnOnLED)
btn_On.grid(row=0, column=0)

btn_Off = tk.Button(root, text="Turn Off", command=turnOffLED)
btn_Off.grid(row=0, column=1)

blinkState = IntVar()
chkBtn_Blink = tk.Checkbutton(root, text = "Blink",variable = blinkState, command = blinkLED)
chkBtn_Blink.grid(row=0, column = 2)

blinkTime = ['50','100','150','200','250','300','350','400','450','500','550','600','650','700','750','800','850']
userDelay = StringVar()
delayMenu = tk.OptionMenu(root,userDelay,*blinkTime)
userDelay.set('800')
delayLabel = tk.Label(root,text="Blinking ms")
delayLabel.grid(row=1,column=0)
delayMenu.grid(row=1,column=1)

root.geometry("400x100")
root.mainloop()
