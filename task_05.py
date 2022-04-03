'''
Show the sum of digits in a list
[12, 1, 2, 3, 5, 8, 13]
'''

def Method_1(aArr):
    Sum = 0
    i = 0
    while(i < len(aArr)):
        Sum += aArr[i]
        i += 1
    print(Sum)

def Method_2(aArr):
    Sum = 0
    for i in aArr:
        Sum += i
    print (Sum)

def Method_3(aArr):
    print(sum(aArr))


Arr = [12, 1, 2, 3, 5, 8, 13]
#Method_1(Arr)
#Method_2(Arr)
Method_3(Arr)
