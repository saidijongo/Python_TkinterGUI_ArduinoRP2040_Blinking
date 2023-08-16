import serial
import tkinter as tk
import time


arduino_port = '/dev/ttyACM0'
baud_rate = 9600


ser = serial.Serial(arduino_port, baud_rate, timeout=1)

def turnOnLED():
    if blinkState.get() == 1:
        blinkLED()
    else:
        ser.write(b'turn_on') 
        
def turnOffLED(): 
    ser.write(b'turn_off') 

def blinkLED():
    if blinkState.get() == 1:
        ser.write(b'blinking')  
        time.sleep(1)
        delay = userDelay.get()
        numBlinks = entryBlink.get()
        dataToSend = delay + '-' + numBlinks
        ser.write(dataToSend.encode())

# creating tkinter window 
root = tk.Tk() 
root.title('ArduinoLED Blink GUI')
root.configure(bg="red")

btn_On = tk.Button(root, text="Turn On", command=turnOnLED)
btn_On.grid(row=0, column=0)

btn_Off = tk.Button(root, text="Turn Off", command=turnOffLED)
btn_Off.grid(row=0, column=1)

blinkState = tk.IntVar()
chkBtn_Blink = tk.Checkbutton(root, text="Blink", variable=blinkState, command=blinkLED)
chkBtn_Blink.grid(row=0, column=2)

blinkTime = ['50', '100', '150', '200', '250', '300', '350', '400', '450', '500', '550', '600', '650', '700', '750', '800', '850']
userDelay = tk.StringVar()
delayMenu = tk.OptionMenu(root, userDelay, *blinkTime)
userDelay.set('800')
delayLabel = tk.Label(root, text="Blinking ms")
delayLabel.grid(row=1, column=0)
delayMenu.grid(row=1, column=1)

entryBlink = tk.Entry(root, width=3)
entryBlink.insert(0, "5")
entryBlinkLabel = tk.Label(root, text="Blinks Count")
entryBlinkLabel.grid(row=2, column=0)
entryBlink.grid(row=2, column=1)

root.geometry("400x100")
root.mainloop()
