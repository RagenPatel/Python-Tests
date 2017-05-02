import random
def getAnswer(ansNum):
    if ansNum == 1:
        return "Maybe \n RandNum = " + str(ansNum)
    elif ansNum >1 and ansNum<5:
        return "wow \n RandNum = " + str(ansNum)
    elif ansNum>=5 and ansNum<=8:
        return "dam \n RandNum = " + str(ansNum)
    elif ansNum>8 and ansNum<=10:
        return "doubtful \n RandNum = " + str(ansNum)

r = random.randint(1,10)
fortune = getAnswer(r)
print(fortune)


print(getAnswer(random.randint(1,10)))
