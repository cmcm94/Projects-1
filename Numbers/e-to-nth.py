import math
places=int(input('how many decimal places?(max 10): '))
if places<11 and places>=0:
    print('{0:.{1}f}'.format(math.e, places))
else:
    print('invalid input')
