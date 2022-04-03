'''
Show first three digits from a list
[12, 1, 2, 3, 5, 8, 13, 21, 34, 55, 9]
'''

def Method_1(aArr):
    print (aArr[0], aArr[1], aArr[2])


def Method_2(aArr):
    i = 0
    while(i < 3):
        print(aArr[i])
        i += 1

def Method_3(aArr):
    for i in range(3):
        print(aArr[i])

def Method_4(aArr):
    for i in aArr[:3]:
        print(i)

Arr = [12, 1, 2, 3, 5, 8, 13, 21, 34, 55, 9]
#Method_1(Arr)
#Method_2(Arr)
#Method_3(Arr)
Method_4(Arr)
