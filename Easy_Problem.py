def problem1(x1,x2) :
    time = []
    for i in x1.split(":") :
        time.append(int(i))
    for i in x2.split(":") :
        time.append(int(i))
    print(time[2]-time[0])
    
def problem2 (word_list) : #Clear
    new_word = word_list.split() #แยกออกจากกัน

    for i in range (len(new_word),0,-1) :
        print(new_word[i-1],end=" ")# print(new_word[::-1])

def problem3 (word) :
    z = word[::-1]
    print("true") if z == word else print("False")

def problem4 (x) :
    count = []
    maximum = 0
    for i in x.upper() :
        if i not in count :
            count.append(i)
            count.append(1)
        if i in count :
            k = count.index(i)
            count[k+1] = count[k+1]+1
    for i in count :
        if type(i) == int :
            if (i) > maximum :
                maximum = i
              
 def problem6(x1,x2) :
    time = []
    for i in x1.split(":"):
        time.append(int(i))
    for i in x2.split(":"):
        time.append(int(i))
    time[1] += time[3]
    time[3] -= time[3]
    time[0] += time[2]
    time[2] -= time[2]
    if time[1] >= 60 :
        time[1] -= 60
        time[0] += 1
    print(str(time[0]).zfill(2),":",str(time[1]).zfill(2))

    print(count)
    print(maximum)
    
def problem7 (x):
    num = []
    sum = 0
    tar = False

    num = list(map(int, str(x)))
    for i in num :
        sum += i
    num = list(map(int,str(sum)))
    sum = 0
    for i in num :
        sum += i
    if sum == 4 :
         print(9-sum,end="")
         print(x)
    else :
        print(x)
 
def problem8 (x1,x2) #NotFinish :
    sum = 0
    for i in range (x1,x2+1) :
        if 100 // i == 0 :
            sum += 365
        elif 400 // i == 0 :
            sum += 366
        else :
            sum += 365
        print(sum)
   
def problem9 (x) :
    calender = [7, 31 ,8 , 31 , 9 , 30 , 10 , 31 , 11 ,30]
    z = x.split("-")
    nowday = int(z[0]) #3
    nowmonth = int(z[1]) #8
    day = 27
    month = 7
    i = 0
    sum = 0
    ep = 0
    epsum = 633
    
    while nowmonth > month or nowday > day:
        if day == calender[i+1] :
            month += 1
            day = 0
            
        sum += 1
        
        if sum == 7 :
            sum = 0
            epsum += 1
            ep += 1
            
        if ep // 5 == 1 :
            epsum -= 1
            
        day += 1
        
    print(epsum)
    
def problem10 (x):
    print(x//35 + x//5)

def problem11 (x):
    num = [1,2,3,5,7,11,13]
    for i in range (14,x+1) :
        if i % 2 != 0 \
                and i % 3 != 0 \
                and i % 5 != 0 \
                and i % 7 != 0 \
                and i % 11 != 0 :
            num.append(i)
    print(len(num))
    
def problem12 (*x):
    boo = "No"
    max = x[0]
    for i in x :
        if i < max :
            boo = "Yes"
        max = i
    print(boo)

def problem13 (x):
    import datetime
    y = x.split("-")
    z = datetime.datetime(2020,int(y[1]),int(y[0]))
    print(z.strftime("%A"))
    
def problem14 (x1,x2) :
    time = []
    dis = 0
    sum = 0

    for i in x1.split(":") :
        time.append(int(i))
    for i in x2.split(":") :
        time.append(int(i))

    if time[0] > 12 :
        time[0] -= 12
    dis = (12 - time[0]) + time[2]
    sum = (dis - 1) * 5
    time[3] = time[3] - sum

    while time[3] < 0 :
        time[3] += 60
        time[2] -= 1
    
    print(str(time[2]).zfill(2),end = ":",)
    print(str(time[3]).zfill(2))
