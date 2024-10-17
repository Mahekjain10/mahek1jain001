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
