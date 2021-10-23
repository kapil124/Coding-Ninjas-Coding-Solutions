## Read input as specified in the question.
## Print output as specified in the question.

p=input()
arr = input().split()
sum = 0
for x in range(len(arr)):
    p=int(arr[x])
    sum=sum+p
print(sum)