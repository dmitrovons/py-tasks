'''
generate and show multiplication table of 4

4x2=08
4x3=12
4x4=16
4x5=20
4x6=24
4x7=28
4x8=32
4x9=36
'''

def Method_1(aDigiht: int):
    i = 2
    while(i <= 9):
        print('%sx%s=%s' % (aDigiht,i, aDigiht*i))
        i += 1


def Method_2(aDigiht: int):
    for i in range(2,9 + 1):
        print('%sx%s=%s' % (aDigiht,i, aDigiht*i))


Method_1(4)
Method_2(4)
