list_a = list()
k = int(input("nhap so luong phan tu: "))
a = [int(input(f'a[{i}]')) for i in range(k)]
for i in range(k):
    list_a.append(a)

n = int(input("nhap so hang n: "))
m = int(input("nhap so cot m: "))

ma_tran = []
if m*n <= k:
    for i in range(n):
        hang = a[(i*m): (i+1)*m] 
        # i = 0 => a[0: m]
        # i = 1 => a[m: 2*m]
        ma_tran.append(hang)
    print(f"ma tran R({n}x{m}:)")
    for hang in ma_tran:
        print(hang)
else:
    print("No")
