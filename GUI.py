import os
import pyfiglet


header = pyfiglet.figlet_format("LAB UI B1.1")
clears = "\n"*100
moveup = "\n"*10
#clears = ""
choice = 0


# os.system("pkill screen")
os.system("screen -d -m -S SW2 /dev/ttyACM0")
os.system("screen -d -m -S SW1 /dev/ttyACM1")
os.system("screen -d -m -S SW3 /dev/ttyUSB0")


while choice != "secretexit":
        print(clears)
        print(header)
        print("Escape-Key: ctl-a-d \n\n")
        print("LAB GUI")
        print("[1] SW1 (DLS1)")
        print("[2] SW2 (DLS2)")
        print("[3] SW3 (ALS1)\n")
        print(moveup)
        choice = input("choice: ")
        if "1" in str(choice):
                os.system("screen -x SW1")
        elif "2" in str(choice):
                os.system("screen -x SW2")
        elif "3" in str(choice):
                os.system("screen -x SW3")