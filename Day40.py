# Exercise 4... Question...




# Write a python program to translate a msg into secret code language. Use the rules below to translate normal English into secret code language... 


# Encoding... 

# if : the word contains atleast 3 characters, remove the first letter and append it at the end now append three random character at the starting and the end

# else : simply reverse the string

# Decoding... 

# if the word contains less than 3 character, reverse it 
# else :
#     remove random character from start and end. Now remove the last letter and append it to the biginning
    
# Your program should aks whether you want to code r decode    









import random
import string

choice = input("Enter 'code' to encode or 'decode' to decode: ").lower()

if choice == "code":
    msg = input("Enter your message: ")
    words = msg.split()
    new_words = []

    for word in words:
        if len(word) >= 3:
            first_letter = word[0]
            word = word[1:] + first_letter

            random_start = ''.join(random.choices(string.ascii_letters, k=3))
            random_end = ''.join(random.choices(string.ascii_letters, k=3))

            word = random_start + word + random_end
        else:
            word = word[::-1]

        new_words.append(word)

    print("Encoded message:", " ".join(new_words))

elif choice == "decode":
    msg = input("Enter your secret message: ")
    words = msg.split()
    new_words = []

    for word in words:
        if len(word) < 3:
            word = word[::-1]
        else:
            word = word[3:-3]
            word = word[-1] + word[:-1]

        new_words.append(word)

    print("Decoded message:", " ".join(new_words))

else:
    print("Invalid choice! Please enter 'code' or 'decode'.")