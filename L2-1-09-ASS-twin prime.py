#twin primes upto given limit

def prime(n):
    prime=True
    for i in range(2,n):
        if(n%i==0):
            prime = False
            break
    return prime
def twin(a,b):
    for k in range(a,b+1):
        j=k+2
        if (prime ( k ) and prime ( j )) :
            print ( {k , j} )

x=int(input("Enter starting value:"))
y=int(input("Enter Ending value:"))
twin(x,y)
