print("Welcome to my game Bhardwaj ji")

playing = input("Do you want to play: ")

if playing !="yes":
    quit()

print("Welcome to the Game play")
score = 0


answer = input ("What is the pet name of Purvit: ")

if answer == "punnu":
    print("Sahi Jawab")
    score += 1

else:
    print("Galat Jawab")

answer = input ("What is the Father's name of Purvit: ")

if answer == "abhishek bhardwaj":
    print("Sahi Jawab")
    score += 1
else:
    print("Galat Jawab")

answer = input ("What is the Mother's name of Purvit: ")

if answer == "ritu bhardwaj":
    print("Sahi Jawab")
    score += 1
else:
    print("Galat Jawab")

answer = input ("What is the birth date of Punnu: ")

if answer == "2 august":
    print("Sahi Jawab")
    score += 1
else:
    print("Galat Jawab")

print("You got " + str(score) + " answers correct")
print("You got " + str((score / 4) * 100) + " %")