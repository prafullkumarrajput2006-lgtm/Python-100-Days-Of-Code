# Dictionary in Python...Ordered 




dict = {
    "name" : "Prafull",
    "age" : 21,
    "clg_name" : "AKGEC",
    "branch" : "CSE(H)",
    "roll_no" : 2300271690045
}

print(dict)
print(type(dict))
print(dict["age"])
print(dict["branch"])
print(dict["roll_no"])                             # if key doesn't exists then it will throw an error
print(dict.get("clg_name"))                        # if key doesn't exists then it will give the value none

print(dict.keys())
print(dict.values())


for key in dict.keys():
    print(f"The value corresponding to the key {key} is {dict[key]}")
    
    
print(dict.items())    
for key, value in dict.items():
    print(f"The value corresonding to the key {key} is {value}")
    
    