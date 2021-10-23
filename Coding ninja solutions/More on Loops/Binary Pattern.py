n=int(input())
for i in range(1,n+1):
    for l in range(n+2-2*i,0,-1):
        print(1,end="")
    print()
    for j in range (n+1-2*i,0,-1):
        print(0,end="")
    print()