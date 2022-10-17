from audioop import findfactor


n=int(input("enter"))
res=1
for i in range(1,n+1):
    res=res*i
print("factorial of",n,"is",res)