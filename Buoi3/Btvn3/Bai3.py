s1 = input("nhap chuoi s1:")
s2 = input("nhap chuoi s2:")
print("chuoi s1: ", s1)
print("chuoi s2: ", s2)

new_s1 = s1[::-1]
print("chuoi s1 sau khi dao nguoc: ",new_s1)
a = -1
b = -1
len_s2 = len(s2.split())

while a < 1 or a > b or b > len_s2:
    a = int(input("nhap a:"))
    b = int(input("nhap b:"))
    if 1 <= a and a < b and b <= len_s2:
        break

chuoi_tmp = s2[a:b+1][::-1]
print(chuoi_tmp)
s2  = s2[0:a] + chuoi_tmp + s2[b+1:]
print(s2)

# s3= []
# for i in range(0,len(s1)):
# #    if s1[i] % 2 == 0:
# #        s3.append(s1[i])
# # print("chuoi s3"%s3)
#     print(s3)


# s4 =[]
# if len(s1)>=len(s2):
#     n = len(s1)
# else:
#     n = len(s2)
# for i in range(n):
#     s4 += s1[i] + s2[i]
# print("chuoi s4:",s4)