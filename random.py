import random

for i in range(5,0,-1):
    print(random.randint(1,10))
    print("i val : "+str(i))
    
    
import sys

while not False:
    print("Type exit to quit.")
    response = input()
    if response == "exit":
        sys.exit()
    print('You typed ' + response + ".")
