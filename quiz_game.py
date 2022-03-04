print("Welcome to the computer refresher quiz!")

playing = input("Do you want to take a break from code and play a little game to refresh your mind? ")

if playing.lower().strip() == "yes" or playing.lower().strip() == "y":
    print("Okay! Lets play! :) ")
else:
    print("Loser.... stop wasting my time!")
    quit()

score = 0

answer = input("What does CPU stand for? ")
if answer.lower().strip() == "central processing unit":
    print("Correct! A gold star for you * ")
    score += 1
else:
    print("Incorrect! Try again")
    while score > 0:
        score -= 1

answer = input("What does RAM stand for? ")
if answer.lower().strip() == "random access memory":
    print("Correct! Another gold star for you * ")
    score += 1
else:
    print("Incorrect! Try again")
    while score > 0:
        score -= 1

answer = input("What does PSU stand for? ")
if answer.lower().strip() == "power supply unit":
    print("Correct! A gold star for you * ")
    score += 1
else:
    print("Incorrect! Try again")
    while score > 0:
        score -= 1

answer = input("In the software development principles, what does DRY stand for? ")
if answer.lower().strip() == "dont repeat yourself":
    print("Correct! A gold star for you * ")
    score += 1
else:
    print("Incorrect! Try again")
    while score > 0:
        score -= 1

answer = input("In the software development principles, what does KISS stand for? ")
if answer.lower().strip() == "keep it simple stupid":
    print("Correct! A gold star for you * ")
    score += 1
else:
    print("Incorrect! Try again")
    while score > 0:
        score -= 1

print("Your total score is " + str(score) + " gold stars!" )

if score >= 4:
    print("You're doing well, keep up the hard work!")
elif score <= 2:
    print("Hmmmm... were you not sleeping in class maestro... ?")
else:
    print("It seems you'll scrape by.... I hope you're having a lot of fun in the process")