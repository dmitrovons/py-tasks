'''
Show first three not even digits from a list
[12, 6, 2, 3, 15, 8, 13, 10, 7]
'''

def Method_1():
    Arr = [12, 6, 2, 3, 15, 8, 13, 10, 7]
    for i in range(len(Arr)):
        if(Arr[i] % 2 == 0):
            print (Arr[i])

def Method_2():
    Arr = [12, 6, 2, 3, 15, 8, 13, 10, 7]
    for i in range(len(Arr)):
        if(Arr[i] % 2 == 1):
            print (Arr[i])

def Method_3():
    Arr = [12, 6, 2, 3, 15, 8, 13, 10, 7]
    Res = 0
    for i in range(len(Arr)):
        Res += Arr[i]
    print (Res)

def Method_4():
    Arr = [12, 6, 2, 3, 15, 8, 13, 10, 7]
    Res = 0
    for i in range(len(Arr)):
        Res += Arr[i]
    print (Res / (len(Arr)))

def Method_5():
    Arr = [12, 6, 2, 3, 15, 8, 13, 10, 7]
    i = 0
    while(i < len(Arr)):
        if(Arr[i] > 2 and Arr[i] < 10):
            print(Arr[i])
        i += 1


#Method_1()
#Method_2()
#Method_3()
#Method_4()
Method_5()