#Password

tries = 5

while(tries>0):
    print("Enter username")
    user = input()
    if(user=="Ragen"):
        print("Enter password")
        if(input()=="pass"):
            print("Welcome to the account")
            tries-=1
            break
        else:
            print("retry.\n You have "+str(tries)+" remaining.")
    else:
        tries-=1
        print("retry.\n You have "+str(tries)+" remaining.")
