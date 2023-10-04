import os as os
import time
from pathlib import Path as path
#5. Image Service reads image-service.txt, erases it, and writes an image path to it

fileName = "image-service.txt"
num = 2
#imgStr = str(num) + ".png"
#print("file is at ",os.path.abspath(imgStr) )




while True:
    #get line from img-srv.txt
    with open('PRNG.txt') as f:
        readRandNum = f.readlines()

    file = open("image-service.txt", mode = 'w') # open img-serv
    #file.write(" ")        #erase img-serv

    if len(readRandNum) > 0:      # dont want to check index of lines before it contains anything!
        randNum = readRandNum[0]
        imgStr = str(randNum) + ".png"
        time.sleep(8)
        #print("file is at ",os.path.abspath() )
        file.write(  os.path.abspath(str(imgStr)     )    )       #img path
