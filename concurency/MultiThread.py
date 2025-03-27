# concurency: its a way to run multiple tasks at the same time but not necessarily simultaneously.
# parallelism: its a way to run multiple tasks simultaneously. its a subset of concurrency. its about doing lots of things at once.
# multi-threading: its a way to achieve concurrency. its about doing lots of things nearly at once.
#  its a way to run multiple tasks at the same time but not necessarily simultaneously.

import threading
import time
import requests
import os
from urllib.parse import urlparse
from datetime import datetime

list = []
threads = []
def calculations(a,b):
    print(f"Addition of two numbers {a} , {b}:",a+b)
    print(f"Sufbtraction of two numbers {a} , {b}:",a-b)
    print(f"Multifplication of two numbers {a} , {b}:",a*b)
    print(f"Division of two numbers {a} , {b}:",a/b)

def takeInput():
    if(len(list) == 0):
        status  = input("Do you want to enter numbers? (y/n):")
        if(status == 'y'):
            a = int(input("Enter first number:"))
            b = int(input("Enter second number:"))
            list.append({"inputa":a,"inputb":b,"status":False})
    elif(len(list) < 1):
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


# file download using multi-threading
def download(url):
    r = requests.get(url, stream=True)

    # Extract filename from URL
    original_filename = os.path.basename(urlparse(url).path)

    # Generate a unique filename using timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]  # Format: YYYYMMDDHHMMSSmmm
    filename = f"{timestamp}_{original_filename}"

    print(f"Downloading file {filename}...")
    time.sleep(2)  # Simulating network delay

    with open(filename, "wb") as file:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)

    print(f"Downloaded {filename}")

urls = ["https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        "https://fileinfo.com/img/ss/xl/jpg_44-2.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/4/41/Sunflower_from_Silesia2.jpg"]
threads = []
for url in urls:
    t = threading.Thread(target=download, args=(url,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
print("All files downloaded")
