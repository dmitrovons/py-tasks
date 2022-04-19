'''
Find and show minimal digit from a list
[12, 6, 2, 3, 15, 8, 13]
'''
def Method_1(aArr):
    Res = 100000000000000000000000000000000000000000000
    i = 0
    while (i < len(aArr)):
        C = aArr[i]
        if (C < Res):
            Res = C
        i += 1
    print (Res)

def Method_2(aArr):
    print (min(aArr))


def Method_3(aArr, aRes):
    i = 0
    while (i < len(aArr)):
        C = aArr[i]
        if (C < aRes):
            aRes = C
        i += 1
    print (aRes)

def Method_4(aArr, aRes):
    for i in range(len(aArr)):
        C = aArr[i]
        if (C < aRes):
            aRes = C
    print (aRes)

def Method_5(aArr, aRes):
    for i in aArr:
       if (i < aRes):
            aRes = i
    print (aRes)




Arr = [12, 6, 2, 3, 15, 8, 13]
Res = float('inf')
Method_1(Arr)
Method_2(Arr)
Method_3(Arr, Res)
Method_4(Arr, Res)
Method_5(Arr, Res)
