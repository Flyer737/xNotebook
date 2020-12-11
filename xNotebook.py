#run this program in the same dir you want your logs to be kept.

'''
If .dat is ever deleted, nothing to worry about, just run this program once,
open the .dat as a text document and edit the '0' with the number
of logs you have. Run the program again. All fixed :)
'''

from os import remove
from datetime import datetime
import time
import calendar
import random

insult = ["Dummy dumb.","Fuck tard!","Stupid.","Moron!","Smooth brain.","Idiot.","Dummy dumb dumb.","Buddy ol' pal.","Silly billy.","You smol brane.","You dunce!","Would you like to try again?"]

def writeLog(x):
    x=x+1  #counting logs
    remove("MyNoteBook.dat")
    file = open("MyNoteBook.dat","w")
    file.write(str(x) + "\n")
    file.close()

    writing=True
    #pre writeing
    file = open(("Log #"+str(x)+".wlog"),"w")
    file.write("Local Time/Date writen: "+time.asctime( time.localtime(time.time()) )+"\n")
    file.write(calendar.month(datetime.now().year,datetime.now().month))
    file.write("\n==\/-\/==\n")
    file.close()

    file = open(("Log #"+str(x)+".wlog"),"a")
    print("\n"+"Writing log #"+str(x))
    print("==='exit' or 'save' to save and exit===")

    while writing:
        write = input()
        if(write=="save" or write=="exit" or write=="e" or write=="s" or write=="x"):
            writing=False
            file.write("==/\-/\==")
            file.close()
            exit()
        else:
            file.write(write+"\n")
            file.close()
            file = open(("Log #"+str(x)+".wlog"),"a")


try:
    file = open("MyNoteBook.dat","r")
    file.close()
except FileNotFoundError:
    file = open("MyNoteBook.dat","w")
    level=0
    file.write(str(level) + "\n")
    file.close()
    
file = open("MyNoteBook.dat","r")
read = file.readline()
level = int(read)
file.close()



while True:
    print("\nMyNotebookLite ver.1.0  -  Type 'help' for list of commands.")
    A = input()
    if A=="help":
        print("(w)rite = write a new log")
        print("(r)ead  = read a created log.")
        print("(e)xit  = closes the application")
    if A=="write" or A=="w":
        if level!=1:
            print("You have "+str(level)+" logs. Create log #"+str(level+1)+" now?")
        else:
            print("You have "+str(level)+" log. Create log #"+str(level+1)+" now?")
        A = input("y/n:")
        if A=="y":
            writeLog(level)
    
    if A=="read" or A=="r":
        if level!=1:
            print("You have "+str(level)+" logs.")
        else:
            print("You have "+str(level)+" log.")
        B="I'm a B"
        while(B!="e"):
            print("What would you like to read?   ('e' to close)")
            B = input("Log #")

            
            
            password="yo"
            '''
            if (B=="9"): #Add password protected files (use B=="log#" to password protect that log)
                
                print("Uh Oh! That log is password protected!")
                try_p = input("Password:")
                if(try_p!=password):
                    print("That password is not correct!")
                    print("Terminating this session in...")
                    tempnum=10
                    for i in range(11):
                        print(tempnum)
                        time.sleep(1)
                        tempnum=tempnum-1
                    exit()
'''
                
            if B!='e':
                try:
                    B = int(B)
                except ValueError:
                    print("That's not a number!")
                    print(random.choice(insult))
                print("\n========================================")
                try:
                    file = open(("Log #"+str(B)+".wlog"),"r")
                    read=file.read()
                    print(read)
                except FileNotFoundError:
                    print("That log has not been created yet!")
                    print(random.choice(insult))
                print("========================================\n")
                file.close()
            
    if A=="exit" or A=="e":
        exit()
    if(A!="help" and A!="write" and A!="read" and A!="exit" and A!="r" and A!="e" and A!="w"):
        print("'"+A+"' is not a valid command.")




















