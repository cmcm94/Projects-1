primes = []
nonprimes = []
primefactor = []
##add factors to primes[]
def factor(num):
    for x in range (2,num):
        if num%x == 0:
             primes.append(x)
             x+=1
        else:
            x+=1
##add non-primes to nonprimes[]
def isprime(num2):
    for y in range (2,num2):
        if num2%y == 0:
            nonprimes.append(num2) 
            exit
        else:
            y+=1
##start
startnum=int(input('Choose a number (must be > zero):  '))
factor(startnum)
primeslen=len(primes)
for z in range (0,primeslen):
    isprime(primes[z])
    z+=1
##get rid of nonprime numbers in primes list
primefactor = list(set(primes) - set(nonprimes))
if not primefactor:
    if startnum<=0:
        print('cannot be 0 or negative')
    else:
        print(startnum,'is prime')
else:
    print(primefactor)
