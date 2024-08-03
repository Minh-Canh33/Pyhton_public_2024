# Bài 1:
# Cho một tuple gồm n phần tử kiểu xâu ký tự nhưng các ký tự đều là các con số từ 0 tới
# 9. Hãy chuyển đổi tuple đó để thu được tuple mới gồm phần tử kiểu số tương ứng.
# Tính trung bình cộng các phần tử trong tuple thu được.
s = []
n = int(input("nhap so luong n:"))
a =[int(input(f"a[{i}]")) for i in range(n)]
for i in range(n):
    s.append(a[i])
a = tuple(s)

temp = list(a)
new_list = []

for i in range(1, n + 1):
   N = float(sum(temp[:i])) / i
   new_list.append(N)
new_tuple = tuple(new_list)
print(new_tuple)
