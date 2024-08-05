input_numbers = input("Nhập các số nguyên: ")  

numbers_tuple = tuple(map(int, input_numbers.split()))  

from collections import Counter  
count = Counter(numbers_tuple)  

result = []  
for number in count:  
    if count[number] % 5 == 0 and count[number] % 10 != 0:  
        result.append(number)  
print(result)

