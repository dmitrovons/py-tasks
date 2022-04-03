'''
Show all digits from a list in reverse order
[12, 1, 2, 3, 5, 8, 13, 21, 34, 55, 9]
'''

def Method_1(aArr):
    i = len(aArr) - 1
    while(i >= 0):
        print(aArr[i])
        i -= 1

def Method_2(aArr):
    Len = len(aArr)
    for i in range(Len):
        Idx = Len - i - 1
        print(Idx, aArr[Idx])

def Method_3(aArr):
    for i in reversed(range(len(aArr))):
        print(i, aArr[i])

def Method_4(aArr):
    for i in reversed(aArr):
        print(i)

def Method_5(aArr):
    print(list(reversed(aArr)))


Arr = [12, 1, 2, 3, 5, 8, 13, 21, 34, 55, 9]
#Method_1(Arr)
#Method_2(Arr)
#Method_3(Arr)
#Method_4(Arr)
Method_5(Arr)
