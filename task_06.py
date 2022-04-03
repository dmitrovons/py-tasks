'''
exchange variables A and B
A = 8
B = 5
'''


def Method_1(aA, aB):
    C = aA
    aA = aB
    aB = C
    print(aA, aB)

def Method_2(aA, aB):
    aA,aB = aB,aA
    print(aA, aB)


A = 8
B = 5

Method_1(A, B)
Method_2(A, B)