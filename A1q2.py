def f(n): 
    s=0
    for i in range(1,n+1):
        if n%i == 0:
           s = s+1
    return(s%2 == 1)
