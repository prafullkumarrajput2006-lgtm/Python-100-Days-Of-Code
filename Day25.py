# Operations on  Tuples... 


# We can't change the tuple, for changing the element or value of the tuple 1st we have to convert it into list and erform the changes and then after performed the changes then again convert it into tuple




countries = ("India", "Japan", "China", "Russia", "USA", "Japan", "England", )

temp = list(countries)
temp.append("Finland")          # add item
temp.pop(3)                     # remove item
temp[2] = "Nepal"               #change item
countries =  tuple(temp)
print(countries)

tuple_1 = (1, 2, 3, 4, 5, 3, 6)
tuple_2 = ("A", "B", "C", "D")
tuple_3 = tuple_1 + tuple_2
print(tuple_3)


print("The number of digit 3 in tuple_1 is : ", tuple_1.count(3))
print("The number of Japan in countries is:", countries.count("Japan"))

print(tuple_1.index(6))

print(len(tuple_2))