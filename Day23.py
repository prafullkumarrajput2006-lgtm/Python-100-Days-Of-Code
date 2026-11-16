# List Methods in Python... Mutable




my_list = [1, 5, 4.5, 5, 12]

print(my_list)


my_list.append(69)
print(my_list)


my_list.sort()                # Not working on String...
print(my_list)


my_list.sort(reverse=True)                 # Not working on String...
print(my_list)


my_list.reverse()                     # Not working on String...
print(my_list)


m = my_list
m[0]= 0
print(my_list)


m = my_list.copy()
m[0]= 0
print(my_list)


my_list.insert(0,999)
print(my_list)


n = [900,1000,1100]
my_list.extend(n)
print(my_list)


x = [100, 200, 300]
print(x)
y =[500, 600, 700]
print(y)
z = x + y
print(z)


