def check(n):
    sum_2 = 0
    for i in range (1,n):
        if n%i==0:
            sum_2 +=i
    return n == sum_2

n = -1
while n < 0:
        n = int(input("nhập số nguyên dương n: "))
        if n > 0:
            break
for i in range (1,n+1):
    if check(i):
        print("các số hoàn hảo : ", i, " ")
