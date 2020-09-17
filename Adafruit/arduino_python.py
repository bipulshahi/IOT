import requests
import serial

ard = serial.Serial("COM7",9600)
q = input("On or Off or Exit to exit")

if q == "exit":
     exit()
elif q == "On":
     ard.write(str.encode("On"))
elif q == "Off":
     ard.write(str.encode("Off"))
else:
     print("Try Again")

     
