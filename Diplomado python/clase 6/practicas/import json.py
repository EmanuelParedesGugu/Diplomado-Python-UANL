import json 

x = {"name":"John", "age":30}
y = json.dumps(x)
z = json.dumps(x, indent=1)
orden = json.dumps(x, indent=4, sort_keys=True)

print(y)
print("-----------------------------------")
print(z)
print("-----------------------------------")
print(orden)