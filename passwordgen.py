import math
import random

wordList = open("wordlist2.txt").read()
wordArr = wordList.splitlines()
password = " "

for i in range(3):
   r= random.randint(0, 438)
   index = r
   if(i==0):
    password += str(wordArr[index])

   else: 
     password += "-"+str(wordArr[index])

print("Your temporary password is " + password)
