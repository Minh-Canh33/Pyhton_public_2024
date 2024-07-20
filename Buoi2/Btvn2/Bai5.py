
def ktra(n):
    m = n
    sum = 0
    while n > 0:
        sum += (n%10)**3
        n//= 10
    return sum == m

n = int(input("nhập số n: "))
for i in range (1,n+1):
    if ktra(i):
        print(i)
