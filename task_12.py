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



Arr = [12, 6, 2, 3, 15, 8, 13]
Res = float('inf')
Method_1(Arr)
Method_2(Arr)
Method_3(Arr, Res)
