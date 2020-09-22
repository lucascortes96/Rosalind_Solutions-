## This one was particularly tough for me to get my head around at first. This is a very elegant solution, although there are other solutions one could use. 
## Fibonacci sequence essentually 
## By defining the two variables a,b and setting them to 1,1 you can essentially store the previous generation's numbers in the 'b' portion of the equation. 
## b+(a*k) is just the fibonacci sequence multiplied by the the number of rabbits per generation. 

def fib(n,k):
    # total number of rabbit pairs
    a,b = 1,1
    for i in range(n-1):
        a,b = b, b+(a*k)
    return a
fib(33, 5)
