val1 = 0
val2 = 0
num=int(input())
while num > 0:
    r = num % 10
    num = num // 10
    if r%2==0:
        val1 = val1 + r
    else:
        val2 = val2 + r

print(val1," ",val2)