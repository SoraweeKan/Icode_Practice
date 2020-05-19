def problemA (x) :
    z = x.split(" ")
    print (int(z[0])+int(z[1]))

def problemB (x) :
    sum = 0
    for i in range (1,x+1,+2) :
        sum += i
    print(sum)

def problemC (x):
    space = x-2
    count = 0
    while x > 0:

        # print("@"*count,end="")
        print(x,end="")
        for j in range (space,0,-1) :
            if space != -4 and space != -2 and space != -1:
                print(" ",end="")


        count = count + 1
        space = space - 2
        if space < -4 :
            for k in range (space+4,0,+1) :
                print(" ", end="")
                # print(k,space2,end="")

        print(x, space)
        x -= 1    
        
def problemD (x) :
    z = 1
    for i in range(x-1,-1,-1) :
        print(" "*i,end="")
        print("#"*z,end="")
        print("")
        z = z + 2
    z = z - 2
    for i in range(1,x+2):
        z = z - 2
        print(" "*i,end="")
        print("#"*z,end="")
        print("")
        
def ProblemH (x) :
    z = x.split()
    sum = 0
    for i in z[0] :
        if i == "[" or i == "(": 
            sum = sum + 1
        else :
            sum = sum - 1
    if sum == 0 :
        print("Yes")
    else : print("No")
