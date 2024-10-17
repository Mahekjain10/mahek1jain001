def evensum(n):
    curr=2
    sum=0
    i=1
    while i<=n:
        sum+=curr
        curr+=2
        i=i+1
    return sum
n=20
print("Sum of first ",n,"Even number is:",evensum(n))
# exchanging the values of variables
def exchange(x,y):
    x,y=y,x
    print("After exchange of x,y")
    print("x:",x)
    print("y:",y)
x=int(input("Enter value of x:"))
y=int(input("Enter value of y:"))
print("Before exchange of x,y")
print("x:",x)
print("y:",y)
exchange(x,y)




