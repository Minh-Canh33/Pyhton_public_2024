
my_list = list()
n = int(input("nhap so luong phan tu : "))
a = [int(input(f'a[{i}]')) for i in range(n)]
for i in range(n):
    my_list.append(a[i])
print(my_list)
#1
x = int(input("nhap so x : "))
tmp = 0
for number in my_list:
    if number == x:
        tmp = tmp + 1
a = my_list.count(x) 
print(a)
print(f" x xuat hien {tmp} lan")
#2
replace_list = [8, 5, 4, 0, 1, 3]
my_list[2:7] = replace_list
print(my_list)
#4
min_list = min(my_list)
max_list = max(my_list)
print(f"gia tri lon nhat {max_list} va gia tri nho nhat {min_list}")
#5
y = int(input("nhap so y : "))
my_list.insert(0,y)
print("List sau khi chen: ",my_list)

#6
# # # a_list = my_list.sort()
# # b_list = sorted(my_list)[::-1]
# # # if my_list == reversed(sorted(my_list)):
b_list = sorted(my_list)[::-1]
if my_list == sorted(my_list):
    print("TĂNG")
elif my_list == b_list:
    print("GIẢM")
else:
    print("No")
#7
my_list1 = [sum(my_list[0:i + 1]) for i in range(n + 1)]
print(my_list1)
#8
new_list = [94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]
new_list = [x if x >= 0 else -x for x in new_list]
sorted_list = sorted(new_list)
print(sorted_list)


