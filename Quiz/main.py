print("Welcome to my computer qiuz!")

playing = input("Wanna play a game?  Yes or No: ")

if playing.lower() != "yes":
    quit()

print("Alrighty! Let's play :)")
print("Each question is worth 1 point unless stated otherwise....GOOD LUCK!")
score = 0

print("Question 1")
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("Question 2")
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("The next question is worth double points!")
print("Question 3")
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 2
else:
    print("Incorrect!")
print("Question 4")
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("Question 5")
answer = input("What is the name of the protagonist in Zelda? ")
if answer.lower() == "link":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("BONUS ROUND worth 3 POINTS!")
print("Last Question")
answer = input("What is the first name of the person who created this quiz game? ")
if answer.lower() == "braden":
    print("Correct!")
    score += 3
else:
    print("Incorrect!")

print("You got  " + str(score) + " points out of 9!")
print("You got " + str((score / 9) * 100) + "%.")

print("List of correct answers")
print("1: Central Processing Unit")
print("2: Graphics Processing Unit")
print("3: Random Access Memory")
print("4: Power Supply Unit")
print("5: Link")
print("6: Braden")
