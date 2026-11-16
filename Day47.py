# Solution of Exercise 4... Day40... 




# Secrect Code language... 





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