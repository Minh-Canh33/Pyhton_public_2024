import pprint
my_dict = {
    'name': 'phương béo',
    "age": "18",
    "score": {
        "math" : "100",
        "physics" : "90"
    }
}
print("my_dict : [name]",my_dict["name"])
print("my_dict : [name]",my_dict["score"])
print("my_dict : [name]",my_dict)
# # pprint.pprint(my_dict)

my_dict['name'] = 'phương béo    '.strip().upper()
print(my_dict['name'],"\n")

my_dict = {
    'name': 'phương béo',
    "age": "18",
    "score": {
        "math" : "100",
        "physics" : "90"
    }
}
for i in my_dict:
    print(i,my_dict[i])
print("\n")

for key, value in my_dict.items():
    print(key,value)

print("\n")
for i,key in enumerate(my_dict):
    print(i,key,my_dict[key])

print("\n")
for key in my_dict.values():
    print(key)

print("\n")
for i, (key,values) in enumerate(my_dict.items()):
    print(i,key, values)