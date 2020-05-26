import os
import pyfiglet
import subprocess, sys
import glob
import serial

header = pyfiglet.figlet_format("LAB UI V1.2")
clears = "\n"*100
moveup = "\n"*10
#clears = ""
choice = 0

### Scratch Zone

def DiscoverSerial():
        os.system("pkill screen") # Disconnect all open connections
        ports = glob.glob('/dev/tty[A-Za-z]*')

        # Find list of available console ports
        serialResult = []
        for port in ports:
                try:
                        s = serial.Serial(port)
                        s.close()
                        serialResult.append(port)
                except:
                        pass
        return serialResult

def CheckForConfig():
        try:
                # See if file exists
                f = open("connections.cfgs", "r")
                file = f.read() 
                return True
        except:
                # If no file
                return False

def InitialSetup():
        ActivePorts = DiscoverSerial()
        ConnectionDB = []
        print(clears)
        print(header)
        print('''
After pressing enter the script will attempt to connect one by one
to all discovered serial connections. Once the connection is opened
by the script and you have determined it is a connection you would like
to connect to, please use ctl-a-d to leave and come back to the script.
(Enter to continue)
                ''')
        input(moveup)
        for x in ActivePorts:
                try:    
                        os.system("pkill screen")
                        os.system("screen -m -S Test {}".format(x))
                except:
                        print("{} Connection error... Moving Forward")
                print('''
If that was a device you would like to add
Please enter its nickname below (NoSpaces)
if not hit enter to move to the next device
                ''')
                nick = input("Nickname:")        
                if nick == "": continue
                ConnectionDB.append([nick, x]) # Append our connection and its nickname
        print(ConnectionDB)
        ans = input("Confirm Connections y/n ?")
        if "y" in ans:
                SaveDB(ConnectionDB)
                return ConnectionDB

def SaveDB(db):
        config = open("connections.cfgs", "w+")
        for x,y in db:
                config.write("{} |-| {} \n".format(x,y))
        

def ReadDB():
        db = []
        f = open("connections.cfgs", "r")
        bit = True
        while bit:
                line = f.readline()
                line = line.replace(" ",""); 
                line = line.replace("\n","")
                line = line.split("|-|")
                if line == ['']: break
                db.append(line)
        return(db)

def ListConnections(db):
        openConnections(db)
        choice = None
        while choice != "exit":
                print(clears)
                print(header)
                print("Escape-Key: ctl-a-d \n\n")
                print("LAB GUI")
                #### Display Connections
                choice = 0
                for x in db:
                        print("{}. {}".format(choice, x[0]))
                        choice += 1
                print(moveup)
                choice = input("choice: ")
                try: choice = int(choice)
                except: continue
                try:
                        makeConnection(choice, db)
                except: print("Not a proper option")

def openConnections(db):
        os.system("pkill screen")
        for x in db:
               os.system("screen -d -m -S {} {}".format(x[0], x[1])) 

def makeConnection(choice, db):
        com = db[choice][0]
        os.system("screen -x {}".format(com))


if __name__ == "__main__":
        db = None
        while db == None: 
                if CheckForConfig():
                        db = ReadDB()
                else: 
                        db = InitialSetup()
        ListConnections(db)