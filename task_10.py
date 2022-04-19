'''
use input() function to get width and height of rectangle and calculate its square and perimeter
'''
def GetRectSquare_1(aWidth, aHeight):
    Square = aWidth * aHeight
    Perimeter = (aWidth + aHeight) * 2
    print('Rectangle size: %s, %s' % (aWidth, aHeight))
    print ('Square: %s' % (Square))
    print ('Perimeter: %s' % (Perimeter))
    

while True:
    Width  = input('Width:')
    if (not Width.isdigit()):
        print('Err')
        continue

    Height = input('Height:')
    if (not Height.isdigit()):
        print('Err')
        continue

    GetRectSquare_1(Width, Height)