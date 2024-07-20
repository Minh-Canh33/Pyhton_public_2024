#a
a = int(input('nhập số  a : '))
dem = 0
if a == 0:
    print ("cần 1 bit")
else: 
    while a!= 0:
        a //= 2
        dem += 1
print("cần :",dem,"bits")

#b
x = 'awesome'
print("Python is",x)
# print("Python is"+x)
print("Python is {}".format(x)) #hàm format thay thế x vào {}
print(f"Python is {x}") # f-string

# c)
import sys
print (sys.version)

