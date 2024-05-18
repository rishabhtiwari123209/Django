def sumOfN(j):
    sum=0
    for i in range(j+1):
        sum+=i
    return sum

i= int(input("enter a number"))
a=sumOfN(i)
print(a)