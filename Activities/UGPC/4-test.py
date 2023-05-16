def Prime(num):
    if(num==1 or num==0):
        return False
    for i in range(2, num):
        if (num%i==0):
            return False
    return num


Input = int(input())
listt = []
for i in range(1,Input + 1):
    if Prime(i):
        print(i)
        listt.append(i)
print(listt)
j = -1
for i in range(len(listt)):
    for j in range()