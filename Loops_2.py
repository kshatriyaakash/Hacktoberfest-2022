# while loop

'''The while loop in python is used to iterate over a block of code as long as the test expression(condition) is true
This loop is generally used when we do not know how many number of times to iterate'''

n=int(input())

while n>=0:
    print(n)
    n-=1 # if this line is not there ,then the loop will run infinite times
