# f-string in Python... Use for string formating... We can use variable in string





# # *** In normal case ... 



# letter = "Hey my name is {} and I'm from {}"

# country = "India"
# name = "Prafull"

# print(letter.format(name, country))









# # *** In abnormal case... 



# letter = "Hey my name is {} and I'm from {}"

# country = "India"
# name = "Prafull"

# print(letter.format(country, name))









# # *** One of these solutions of this Problem... Provide numbering in {}... 




# letter = "Hey my name is {1} and I'm from {0}"

# country = "India"
# name = "Prafull"

# print(letter.format(country, name))









# # Using f-string... use variable in string...



# name = "Prafull Rajput"
# country = "India"

# print(f"Hey my name is {name} and I'm from {country}")









# # *** If we don't want to print the actual value in string... 



# name = "Prafull Rajput"
# country = "India"

# print(f"We use f-string like this : Hey my name is {{name}} and I'm from {{country}}")










# # *** in float value... Without f-string



# txt = "For only {price:.5f} dollars!"
# print(txt.format(price = 96.02302390122))









# # *** in float value... Using f-string... 


# price = 98.4432442392021
# txt = f"For only {price:.5f} dollars!"
# print(txt)
# print(type(f"{2*30}"))









