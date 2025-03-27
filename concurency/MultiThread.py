# concurency: its a way to run multiple tasks at the same time but not necessarily simultaneously.
# parallelism: its a way to run multiple tasks simultaneously. its a subset of concurrency. its about doing lots of things at once.
# multi-threading: its a way to achieve concurrency. its about doing lots of things nearly at once.
#  its a way to run multiple tasks at the same time but not necessarily simultaneously.

import threading
import time

list = []
threads = []
def calculations(a,b):
    print(f"Addition of two numbers {a} , {b}:",a+b)
    print(f"Sufbtraction of two numbers {a} , {b}:",a-b)
    print(f"Multifplication of two numbers {a} , {b}:",a*b)
    print(f"Division of two numbers {a} , {b}:",a/b)

def takeInput():
    if(len(list) < 3):
        a = int(input("Enter first number:"))
        b = int(input("Enter second number:"))
        list.append({"inputa":a,"inputb":b,"status":False})
    else:
        print("List is full")

def showInput():
    time.sleep(4)
    if len(list) > 0:
        for x in list:
            if(x["status"] == False):
                # update status
                x["status"] = True
                t = threading.Thread(target=calculations, args=(x["inputa"],x["inputb"]))
                threads.append(t)
                t1 = threading.Thread(target=takeInput)
                threads.append(t1)
                t2 = threading.Thread(target=showInput)
                threads.append(t2)
                t.start()
                t1.start()
                t2.start()
            
   

takeInputThread = threading.Thread(target=takeInput)
showInputThread = threading.Thread(target=showInput)
takeInputThread.start()
showInputThread.start()

takeInputThread.join()
showInputThread.join()

for t in threads:
    t.join()
