n=int(input()) #take the input number

if n==2: # 2 is the only even prime
    print("Prime number")

elif n<=1 or n%2==0: # if a number is negative or even or one it is not prime
    print("Not a prime number")
else:
    for i in range(3,int(n**0.5)+1,2): # check for odd factors from 3 to sqrt(n)
        if n%i==0: # if n is divisible by any of these factors it is not prime
            print("Not a prime number")
            break
    else:
        print("Prime number") # if no factors found, it is prime