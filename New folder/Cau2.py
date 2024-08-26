k = -1
while k < 0 :
    k = int(input('nhập số nguyên dương: '))
    if k > 0 :
        break


def sohoanhao(num):
    return sum(int(digit) for digit in str(num)) == 10

def timsohoanhao(k):
    count = 0
    num = 1
    while True:
        if sohoanhao(num):
            count += 1
            if count == k:
                return num
        num += 1

result = timsohoanhao(k)
print(f"Số hoàn hảo thứ {k} là: {result}")




    
    




