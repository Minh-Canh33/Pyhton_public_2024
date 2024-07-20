import pprint
# a = input('mystring')
# b = 5
# print(type(a),a,sep="\n")


# a ="i love pyhton"
# b = 5
# # print(a+b)
# print(a)
# print(a[0:6])
# print(a[:6])
# sliced_string = a[0:6] # cắt đoạn
# print(len(sliced_string))
# #print(type(a),a,sep="\n")

# a = "i love python"
# print("trước khi thay đôi= ",a)

# list giống mảng
# # my_list = [1,2,3,'helllo','hi']
# print('my list', my_list)
# print("type",type(my_list))
# print("my_type[0]",my_list[0])
# print("my_type[1:3]",my_list[1:3])
# print("my_type[1:4]",my_list[0:5])


# my_dict = {
#     '2023601261'{
#       "ten":"an",
#     "gioitinh":"nu",
#     "lop":"ktpm",
#     "namsinh": 2005  
#     } 
# }

# pprint.pprint(my_dict)
# print(my_dict)

#phép tính, so sánh
# a = int(input("nhap so nguyen a: "))
# b = int(input("nhap so nguyen b: "))
# print("a + b = ",a+b)
# #// lấy phần nguyên
# #% lấy phần dư
# # ** là lũy thừa

# print("a lon hon b",a > b)


# # toán tử logic
# a = int(input("nhap so a: "))
# b = int(input("nhap so b: "))
# c = int(input("nhap so c: "))
# my_list = [1,2,3,'phuong']
# print(a > c and a+c>b)
# print(a < c or b > a)
# print('phuong' in my_list)
# if('phuong' in my_list):
#     print("<3")
# else:
#     print("sauw")

#toan tử nhận dạng
# e = [1,2,3]
# f = [1,2,3]
# print(type(e))
# print(id(e))
# print(e==f)
# print(e is f)

# if 6 >4:
#     print("dung")
#     print("phuong")
# elif:
#     print("")
# else:
#     print("")

# a = 4
# # result = 1
# # if(a%2==0):
# #     result = a*2
# # else:
# #     result = a*3
# # print("result = ",result)

# result = a*2 if a%2==0 else a*3
# print(result)

#vong lặp
# my_list = [1,2,3,'hêlo','phương']
# for index, values in enumerate(my_list):
#     print(index,values)

# for i in step(0,10,1):
#     print(i,end=' ')

a = 0
while a<10:
    a+=1
    if a==5:
       continue
    print(a,end='')