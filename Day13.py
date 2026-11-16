# String Methods... Strings are Immutable... these methods doesn't change the string, they generates new copy of the string 



name = "Prafull Kumar Rajput"

print(len(name))
print(name.upper())
print(name.lower())
print(name.replace("Prafull", "Lalla"))
print(name.split(" "))

blog_Heading = "introduction to js"

print(blog_Heading.capitalize())
print(blog_Heading.center(100))
print(name.count("a"))
print(name.endswith("!!!"))
print(name.find(" K "))
print(name * 3)
print("Prafull" in name)
print("Saini" in name)
print("Pal" not in name)
print(name == blog_Heading)
print(name.startswith("Prafull"))
print(name.swapcase())
