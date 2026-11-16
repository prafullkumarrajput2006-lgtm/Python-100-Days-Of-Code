# Dictionary Methods in Python.. 




ep_1 = {
    101 : 95,
    102 : 97,
    103 : 98,
    104 : 45, 
    105 : 85,
    106 : 86
}

ep_2 = {
    201 : 45,
    202 : 75,
    203 : 79, 
    204 : 15,
    205 : 49,
    206 : 48
}

print(ep_1)
print(ep_2)

ep_1.update(ep_2)            # for putting the value of ep_2 in ep_1
print(ep_1)


ep_2.pop(205)
print(ep_2)

ep_1.popitem()              # for removing last element
print(ep_1)

