#askhsh 2
import random

def fibonacci(n):
    a = 0
    b = 1

    if n==0:
        return a
    elif n==1:
        return b
    else:
        for i in range(1,n):
            c=a+b
            a=b
            b=c
        return b


elegxos=False
while not elegxos:
    n=input("Give the number of the fibonacci saquence")
    n=int(n)
    if n>=0:
        elegxos=True
    else:
        print("Give another number")



fn=(fibonacci(n))
if fn==1:
    print ("The", n, "number of fibonacci sequence is", fn ,"and is not a prime number")
else:
    i=0
    prime=True
    while i<20 and prime==True:
        a=random.randint(1,fn)
        if a**fn%fn==a%fn:
            i=i+1
        else:
            prime=False

    if prime==True:
        print("The", n, "number of fibonacci sequence is",fn, "and is a prime number")
    else:
        print("The", n, "number of fibonacci sequence is", fn ,"and is not a prime number")
