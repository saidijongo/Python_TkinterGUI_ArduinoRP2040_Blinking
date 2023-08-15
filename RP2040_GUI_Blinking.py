import serial
import tkinter as tk

arduino_port = '/dev/ttyACM0'
baud_rate = 9600

ser = serial.Serial(arduino_port, baud_rate, timeout=1)

def turnOnLED():
    print("Sent Command: ON")
    ser.write(b'turn on')
    if blinkState.get() == 1:
        blinkLED()

def turnOffLED():
    print("Sent Command: OFF")
    ser.write(b'turn off')

def blinkLED():
    if blinkState.get() == 1:
        print("Sent Command: BLINKING")
        ser.write(b'blinking')

root = tk.Tk()
root.title('Arduino InbuiltLED Blinking')

root.configure(bg='lightblue')

on_button = tk.Button(root, text="Turn On", command=turnOnLED)
on_button.grid(row=0, column=0)

off_button = tk.Button(root, text="Turn Off", command=turnOffLED)
off_button.grid(row=0, column=1)

blinkState = tk.IntVar()
chkBtn_Blink = tk.Checkbutton(root, text="Blink", variable=blinkState, command=blinkLED)
chkBtn_Blink.grid(row=0, column=2)

root.geometry("300x100")
root.mainloop()
