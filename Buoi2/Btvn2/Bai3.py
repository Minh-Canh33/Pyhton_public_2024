#3
import math
#a
n = int(input("nhập số n: "))
sum = 0
for i in range(1,n+1):
    if i % 2 == 0:
        sum  = sum - i
    if i % 2 != 0:
        sum += i
print("Tổng dãy S(n): ",sum)

#b
n = int(input("nhập số n: "))
sum = 0
for i in range(1,n+1):
    sum += 1.0/i
print("Tổng dãy S(n): ",sum)

#c
a = int(input("nhap gia tri a: "))
b = int(input("nhap gia tri b: "))
c = int(input("nhap gia tri c: "))
denta = b*b-4*a*c
if a == 0:
    print("nghiệm của phương trình là x = ",c/b)
else:
    if denta > 0:
        print("phương trình có 2 nghiệm x1 : " ,(-b + denta**(0.5))/(2*a))
        print("phương trình có 2 nghiệm x1 : " ,(-b - denta**(0.5))/(2*a))
    elif denta == 0:
        print("phương trình có nghiệm kép x = ",-b/(2*a))
    else:
        print("phương trình vô nghiệm")


