import random

wordList = open("wordlist2.txt").read()
wordArr = wordList.splitlines()
password = " "
i = 0

while(len(password) < 16 or i < 3):
  r= random.randint(0, len(wordArr))
  index = r
  if(i==0):
    password += str(wordArr[index])

  else: 
    password += "-"+str(wordArr[index])
  i+=1
    
print("Your temporary password is " + password)
