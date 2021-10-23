n=int(input())
i=1
k=n
while i<=n:
    j=1
    s=chr(ord('A') + k - 1)
    while j<=i:
        charp = chr(ord(s) + j - 1)
        print(charp ,end='')
        j=j+1
    k=k-1
    print()
    i=i+1