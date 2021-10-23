n=int(input())
i=1
print(1)
while i<=n-1:
    print(i,end="")
    num_2=2
    while num_2<=i: #no of Colums
        print("0",end="")
        num_2+=1
    print(i)
    i=i+1