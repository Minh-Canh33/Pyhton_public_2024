t2 = ("hello", 1, 2, ["nguyễn, lê, hà, phương",3,4])

print(f"t2 = {t2}")
t2 = list(t2)
t2[0]="hi"
print(f"t2 = {t2}")
t2 = tuple(t2)

#set
s = {9,8,7,4,8,5,6,3,1,0,2,5,4,1}
a = {1,2,3,4,5}
print("\n",s)
s.add(10)
print("\n",s)
s.update([90,80,78])
print("\n",s)
s.remove(78)

print("\n",s.pop())
print("\n",s)
# s.clear()
# print("\n",s)
s.discard(90)
print("\n",s)
# s.issubset(a)
# print(a.issubset(s))
# print(s.issubset(a))
print(s.issuperset(a))
b = {"nguyen, le, ha, phuong"}
#phép hợp union

c = b.union(a) # kết hớp 2 cái thành 1
a = {"lục", "lam", "chàm","đỏ"}
s = {"đỏ", "cam", "vàng"}
print(f"c= {c}")
print(f"d1 = {a|s}") #phép hợp
print(f"d2 = {a-s}") #trừ đi cái giống
print(f"d3 = {a&s}") # phép giao
print(f"d4 = {a ^ s}") #in ra cái không trùng nhau ở 2 set

#string = "hoc lap trinh Python cung HIT o o o o"
#cout ('h','o','c',....'I','T')
string = "hoc lap trinh Python cung HIT o 1 1 o"
s = []
for char in string: 
    if char == " ": 
        continue
    s.append(char)
print(f"s1 = {s}") 

s2 =[]
for index in range (len(string)):
    if string[index] == " ":
        continue
    s2.append(string[index])
print(f"s2 = {tuple(s2)}")

s3 = (char for char in string if char is not " ")
print(f"s3 = {tuple(s3)}")

sum = 0
osscurences_char_o = [sum + 1  for char in string if char == "o"]
print(f"osscurences = {len(osscurences_char_o)}")
osscurences_char_o = (sum + 1  for char in string if char is " ")
print(f"osscurences = {len(tuple(osscurences_char_o))}")
osscurences_char_o = (char  for char in string if char is " ")
print(f"osscurences = {tuple(osscurences_char_o)}")
osscurences_char_o = [1  for char in string if char == "1"]
print(f"osscurences = {len(osscurences_char_o)}")

tuple = {44,48,2,3,5,4,7,8,9,7}
s =  sorted(list(tuple))[::-1]
print(s)
print(s[1])