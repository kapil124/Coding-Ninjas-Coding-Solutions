n=int(input())
i=1
while i<=n:
    j=1
    s=chr(ord('A') + i - 1)
    while j<=i:
        charp = chr(ord(s) + j - 1)
        print(charp ,end='')
        j=j+1
    print()
    i=i+1