'''
Find and show maximal digit from a list
[12, 6, 2, 3, 15, 8, 13]
'''
def Method_1():
    Arr = [12, 6, 2, 3, 15, 8, 13] 
    Res = None
    i = 0
    while (i < len(Arr)):
        C = Arr[i]
        if (Res == None) or (C > Res):
            Res = C
        i += 1
    print (Res)

Method_1()

