x=1
y=1
z=0
places=int(input('how many numbers?(max 15): '))
if places==1:
    print('0')
elif places<16 and places>1:
    print('0', end='  ')
    for places in range (1,places):
        if z%2>0:
            print(x, end='  ')
            x=x+y
            z+=1
        else:
            print(y, end='  ')
            y=x+y
            z+=1
else:
    print('invalid input')
