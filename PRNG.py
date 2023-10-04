#close main before prng.py
import random as rand
import time

imgLib_size = 6
randNum = rand.randint(1, 663)
if randNum > 6:
    corct_size = randNum % imgLib_size

print("generating rand num: ", randNum)

fileName = "PRNG.txt"

num = 0

while num < 1000000:
    file = open("PRNG.txt", mode='r'); #open returns file object
    num += 1;
    with open('PRNG.txt') as f:
        lines = f.readlines()

    #print("lines?", lines)

    if lines == ['run']:
        print("writing!!!!!!!!")
        time.sleep(5) #ladies and gentlemen, we got him
        file = open("PRNG.txt", mode='w');
        file.write(str(randNum)) #corrct sizw
        file.flush()

#file.write("Muhammed Sumbol")
file.close()