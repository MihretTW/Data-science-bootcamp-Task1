x0=int(input("Enter the first number: ")) # take the first number as input
x1=int(input("Enter the second number: ")) # take the second number as input
n=int(input("Enter the number of terms: ")) # take the number of terms as input

Fibonacci_sequence=[x0, x1] # initialize the Fibonacci sequence with the first two numbers
for i in range(2,n):
    Fibonacci_sequence.append(Fibonacci_sequence[i-1]+Fibonacci_sequence[i-2]) # calculate the next term by adding the previous two terms and append it to the sequence
print(Fibonacci_sequence) # print the Fibonacci sequence up to n terms