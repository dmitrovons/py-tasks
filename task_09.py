'''
use input() function to get month number in a range from 1 to 12 and show its season name

conditions are:
3, 4, 5 - spring
6, 7, 8 - summer
9, 10, 11 - autumn
12, 1, 2 - winter
'''

def Method_1(aMonthNo):
    Spring = [3,4,5]
    Summer = [6,7,8]
    Autumn = [9,10,11]
    Winter = [12,1,2]

    if (aMonthNo in Spring):
        print ('Spring')
    elif (aMonthNo in Summer):
        print ('Summer')
    elif (aMonthNo in Autumn):
        print('Autumn')
    elif (aMonthNo in Winter):
        print ('Winter')
    else:
        print ('number %s out of range ' % (aMonthNo))

def Method_2(aMonthNo):
    if(aMonthNo >= 3) and (aMonthNo <= 5):
        print ('Spring')
    elif(aMonthNo >= 6) and (aMonthNo <= 8):
        print ('Summer')
    elif(aMonthNo >= 9) and (aMonthNo <= 11):
        print('Autumn')
    elif(aMonthNo == 12) or (aMonthNo == 1)  or (aMonthNo == 2):
        print ('Winter')
    else:
        print ('%s is not a valid month' % (aMonthNo))


#Method_1(13)
Method_2(1)

