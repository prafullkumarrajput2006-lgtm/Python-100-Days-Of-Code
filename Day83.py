# Excercise 9... Question... Good Morning to Everyone... 



# # Write a program to pronounce list of the names using win32 APi. If You are given a lit i as follow... 


# l = ["Prafull", "Chanchal", "Kamal", "Harsh", "Kapil", "Udit"]

# # outpur... 


# Good Morning Prafull
# Good Morning Chanchal








import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

names = input("Give the list whose to wish: ")

l = names.split(",")

for name in l:
    name = name.strip()
    speaker.Speak(f"Shout out to {name}")