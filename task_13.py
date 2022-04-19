'''
Find and show maximal digit from a list
[12, 6, 2, 3, 15, 8, 13]
'''
def Method_1(aArr, aRes):
    i = 0
    while (i < len(aArr)):
        C = aArr[i]
        if (aRes == None) or (C > aRes):
            aRes = C
        i += 1
    print (aRes)

def Method_2 (aArr, aRes):
    for i in range(len(aArr)):
        C = aArr[i]
        if (aRes == None) or (C > aRes):
            aRes = C
    print (aRes)

def Method_3 (aArr, aRes):
    for i in aArr:
        C = i
        if (aRes == None) or (C > aRes):
            aRes = C
    print (aRes)

def Method_4 (aArr):
    print (max(aArr))


Arr = [12, 6, 2, 3, 15, 8, 13] 
Res = None
Method_1(Arr, Res)
Method_2(Arr, Res)
Method_3(Arr, Res)
Method_4(Arr)

