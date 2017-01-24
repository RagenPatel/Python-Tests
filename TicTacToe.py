def printTable():
    print("  0 1 2")
    for i in range(3):
        print(str(i), end='')
        for k in range(4):
            if k<3:
                print("| ",end='')
            else:
                print("|") 



def printWithArr(arr, pos):
    print("  0 1 2")
    for i in range(3):
        print(str(i), end='')
        for k in range(4):
            if k<3:
                print("|"+str(arr[k]),end='')
            else:
                print("|") 
 
arr = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
print(arr)

printTable()

print(arr)

x = 1
while(True):
    pos = -1
    if x ==1:
        print('where would you like to place "O"?')
        print("column (0, 1, 2) left vertical #s? ",end='')
        col = input()
        print(col)
        print('row (0, 1, 2)? to horizontal ', end='')
        row = input()

        if(col==0):
            print("col = 0")
            if(row==0):
                pos = 1
                arr[pos] = 'O'
                print('Pos = ' + str(pos))
            elif(row==1):
                pos = 2
                arr[pos] = 'O'
            elif(row==2):
                pos = 3
                arr[pos] = 'O'
        elif(col==1):
            if(row==0):
                pos = 4
                arr[pos] = 'O'
            elif(row==1):
                pos = 5
                arr[pos] = 'O'
            elif(row==2):
                pos = 6
                arr[pos] = 'O'
        elif(col==2):
            if(row==0):
                pos = 7
                arr[pos] = 'O'
            elif(row==1):
                pos = 8
                arr[pos] = 'O'
            elif(row==2):
                pos = 9
                arr[pos] = 'O'
                
        printTable()
        
        x-=1
        
    elif x ==0: 
        print('where would you like to place X?')
        print("column (0, 1, 2)? left vertical #s?",end='')
        col = input()
        print('col: '+str(col))
        print('row (0, 1, 2)? top horizontal ', end='')
        row = input()
        print('row: '+str(row))

        if(col==0):
            print("col = 0")
            if(row==0):
                pos = 1
            elif(row==1):
                pos = 2
            elif(row==2):
                pos = 3
        elif(col==1):
            if(row==0):
                pos = 4
            elif(row==1):
                pos = 5
            elif(row==2):
                pos = 6
        elif(col==2):
            if(row==0):
                pos = 7
            elif(row==1):
                pos = 8
            elif(row==2):
                pos = 9

        arr[pos] = 'X'
        
        x+=1
