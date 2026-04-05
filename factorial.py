n=int(input()) #accepts a number

factorial=1 # a variable to store the factorial
for i in range(1,n+1):
    factorial*=i # multiply the current value of factorial with i to get the factorial of n 
print(factorial)

