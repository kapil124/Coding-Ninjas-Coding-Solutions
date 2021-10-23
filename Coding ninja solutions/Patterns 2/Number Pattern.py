n=int(input())
totalspace=n*2-2
row=1
while(row<=n):
    column=1
    while column<=row:
        print(column,end='')
        column=column+1
    space=1
    while space<=totalspace:
        print(' ',end="")
        space+=1
    totalspace-=2
    column=row
    while column>0:
        print(column,end='')
        column-=1
    row+=1
    print()