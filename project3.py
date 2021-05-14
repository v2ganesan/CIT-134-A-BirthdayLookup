def power(x,n):
    if(n==1):
        return(x)
    if(n!=1):
        return (x*power(x,n-1))
x=float(input("Base: "))
n=int(input("Exponent: "))
print("Result:",power(x,n))