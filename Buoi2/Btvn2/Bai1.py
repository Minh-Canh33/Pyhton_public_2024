# #bài 1
#a
a = -1
sum = 0
while a < 0:
    a = int(input("nhập số nguyên dương a: "))
    if a > 0:
        break
length_a = len(str(a))
# print("đô dài của a: ",n)
for i in range (0,length_a):
    sum = sum + (a%10)
    a//=10
print("tổng các chữ số trong a: ",sum)

#b
n = -1
sum_2 = 0
while n < 0:
    n = int(input("nhập số nguyên dương n: "))
    if n > 0:
        break
for i in range (1,n+1):
    if n%i==0:
        sum_2 +=i
# for i in range (1,(int)(n/2)+1):
#     if n % i == 0:
#         sum_2 +=i
print("tổng các ước của n: ",sum_2)

#c
print("nhập 3 cạnh của tam giác a,b,c ")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a < b+c and b < a+c and c < a+b:
    if a == b != c or a == c != b or c == b != a:
        print("3 cạnh tạo thành tam giác cân")
    elif a == b == c:
        print("3 cạnh tạo thành tam giác đều")
    elif a*a + b*b == c*c or a*a + c*c == b*b or a*a == b*b + c*c:
        print("3 cạnh tạo thành tam giác vuông")
    elif a*a + b*b < c*c or a*a + c*c < b*b or a*a > b*b + c*c:
        print("3 cạnh tạo thành tam giác tù")
    else:
        print("3 cạnh tạo thành tam giác nhọn")
else:
    print("3 cạnh không tạo thành tam giác")