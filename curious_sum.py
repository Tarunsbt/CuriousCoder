def sum(n):
    
    if(n%10==n):
        return n
    else:
        return n%10+sum(n//10)
print(sum(234))

