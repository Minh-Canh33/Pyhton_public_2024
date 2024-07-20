#Bài 4
n = int(input("nhập số n: "))
def dayfibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        return dayfibo(n-1)+dayfibo(n-2)
print(dayfibo(n))
