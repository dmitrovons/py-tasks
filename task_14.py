'''
Show not even digits from a list
[12, 6, 2, 3, 15, 8, 13]
'''
def Method_1(aArr):
    i = 0
    while (i < len(aArr)):
        if(aArr[i] %2 != 0):
            print(aArr[i])
        i += 1

def Method_2(aArr):
    for i in range(len(aArr)):
        if(aArr[i] %2 != 0):
            print(aArr[i])

def Method_3(aArr):
    for i in aArr:
        if(i %2 != 0):
            print(i)

Arr = [12, 6, 2, 3, 15, 8, 13]
Method_1(Arr)
Method_2(Arr)
Method_3(Arr)
