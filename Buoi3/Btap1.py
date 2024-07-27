# Nhập một xâu ký tự bất kỳ từ bàn phím. Cho biết xâu vừa nhập có bao nhiêu từ 
# (giả sự từ là các cụm ký tự ngăn cách nhau bởi dấu cách)

# my_string = input("nhập xâu kí tự bất kì: ")
# list_string = my_string.split()
# print("\n")
# print("original string: ",my_string)
# print("list string: ",list_string)
# print("len my_string: ",len(list_string))

# #tổng các số lẻ  và số chẵn sử dụng list comprehension1-> e5
# import time
# start_time = time.time()
# my_list = list()
# for i in range(1, int(1e5)):
#     if i %2 == 0:
#         my_list.append(i)
# print("\n"'sum my_list: ',sum(my_list))
# end_time = time.time()
# print("time to calculate : ", end_time - start_time)

# start_time = time.time()
# n_iterable = int(1e7)
# start_time = time.time()
# my_list1 = (i for i in range(1,n_iterable) if i%2  == 0)
# end_time = time.time()
# print('time list',end_time - start_time)

# old_list = [1,2,3]
# old_list1 = [1,2,3]
# print("\n" "id(old_list)",id(old_list))
# new_list = old_list.copy()
# print( "id(new_list)",id(new_list))
# print( "id(old_list)",id(old_list))

# old_list.append(1000)
# print("old_list", id(old_list))
# print( "id(new_list)",id(new_list))

# Nhập vào từ bàn phím một list a, b gồm n số nguyên. Sắp a tăng dần và in ra màn hình
# Nhân ban b lên gấp đôi, đảo ngược b sau đó ghép a với b để thu được list c.

n = int(input("nhập vào số lượng n: "))
# a = []
# for i in range(n):
#     x = int(input())
#     a.append(x)
a = [int(input(f'a[{i}]')) for i in range(n)]
b = [int(input(f'b[{i}]')) for i in range(n)]

# for i in range(n):
a.sort()
print("day a sau sx: ", a)
# a_sorted = sorted(a,reverse = false)[::-1]
# print(a_sorted)

b = [i**2 for i in range(n)]
print("day b sau khi dao: ",b[::-1])

c = a+b
print ("ghep a voi b = c: ",c)



