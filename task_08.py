'''
generate and show following sequence
 - using range() function 
 - using while
6, 9, 12, 15, 18
'''


def Method_1(aStart, aEnd, aStep):
    for i in range(aStart,aEnd + 1,aStep):
        print(i)

def Method_2(aStart, aEnd, aStep):
    while(aStart <= aEnd):
        print(aStart)
        aStart += aStep
        

Method_1(6, 18, 3 )
#Method_2(6, 18, 3)
