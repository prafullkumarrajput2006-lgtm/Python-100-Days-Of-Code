# Set Methods in Python... 




s1 = {1, 2, 3, 4, 5, 12, 13, 14}
s2 = {3, 4, 5,11, 12, 13, 14, 15}

print(s1, s2)
print(s1.union(s2))
print(s1.intersection(s2))


# *** Symetric Difference... (A union B) - (A intersection B)

print(s1.symmetric_difference(s2))

print(s1.difference(s2))
print(s2.difference(s1))

print(s1.isdisjoint(s2))
print(s1.issuperset(s2))

s1.remove(13)
print(s1)

s1.discard(13)
print(s1)

if 14 in s1:
    print("14 is present in s1")
else:
    print("14 is not present in s1")
    
    





# # More methods... 


# 1. pop()
# 2. del()
# 3. update()
# 4. add()
# 5. remove()
# 6. discard()
# 7. clear()
