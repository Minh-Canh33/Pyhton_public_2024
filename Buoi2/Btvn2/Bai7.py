def Tong(n):
    sum = 0
    for i in range (1,n):
        if n % i == 0:
            sum += i
    return sum

# def check(n):
#     for i in range(1,n+1):
#         sum_i = Tong(i)
    
#     if sum_i < n and sum_i != i:
#         sum_j = Tong(sum_i)
#         if sum_j == i:
#             return True
#     return False

def check(n):
    sum_i = Tong(n)
    if sum_i > n and Tong(sum_i) == n:
        return True
    return False

n = int(input("nhập số nguyên n: "))
checked = set()
print("các cặp số amicable: ")
for i in range(1,n+1):
    if i not in checked and check(i):
        sum_i = Tong(i)
        checked.add(i)
        checked.add(sum_i)
        print(i,sum_i)
