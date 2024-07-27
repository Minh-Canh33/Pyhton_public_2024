N = int(input("nhập số lượng dãy: "))
l = list (map(int , input().split()))

Ba = []
dem = 0
for i in range(N):
    t = l[i]%10
    if t == 1 or t == 3 or t == 5 or t == 7 or t == 9:
        dem +=1
        Ba.append(l[i])
print(dem)
Ba.sort()
print(Ba)