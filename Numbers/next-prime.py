count=2
answer= 'y'
##returns yes if number is prime
def isprime(num):
    prime='yes'
    for x in range (2,num):
            if num%x == 0:             
                prime='no'
                x=num
            else:
                x+=1
    return prime

##start
while answer == 'y':
    answer=input('Find next prime? (y/n):  ')
    if not answer == 'y':
        quit
    else:
        print(count)
        count+=1
        while isprime(count) is 'no':
            count+=1
