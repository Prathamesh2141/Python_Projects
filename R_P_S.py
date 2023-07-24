import random

print("🧡🧡🧡Rock✊  Paper🖐️  Scissor✌️🧡🧡🧡")
print("🧡🧡🧡get Ready for the game🧡🧡🧡")
choice = ["Rock", "Paper", "Scissor"]
choiEmoji = {"Rock": "✊",
       "Paper": "🖐️",
       "Scissor": "✌️"}
Exit = ""
camWin = 0
youWin = 0
tie = 0
turn = int(input("Plzz Enter a number do you want to play: "))
while turn:

    while True:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        userIn = input("Enter Rock,Paper or Scissor: ")
        if (userIn == "Rock" or userIn == "Paper" or userIn == "Scissor"):
            break
        else:
            print("Please Enter Valid input 🥸🥸🥸")

    youIn = userIn[:]
    comIn = random.randint(0, 2)
    CIN = choice[comIn]
    if (userIn == "Rock"):
        userIn = choiEmoji["Rock"]
    elif (userIn == "Paper"):
        userIn = choiEmoji["Paper"]
    elif (userIn == "Scissor"):
        userIn = choiEmoji["Scissor"]
    print("User input: ", userIn)
    if (comIn == 0):
        comIn = choiEmoji["Rock"]
    elif (comIn == 1):
        comIn = choiEmoji["Paper"]
    elif (comIn == 2):
        comIn = choiEmoji["Scissor"]
    print("Computer input: ", comIn)
    if (CIN == "Rock" and youIn == "Paper"):
        print("Congratulation, You Win Brooo")
        youWin += 1
    elif (CIN == "Paper" and youIn == "Rock"):
        print("Computer Win Brooo try again, Best Luckk!!")
        camWin += 1
    elif (CIN == "Paper" and youIn == "Scissor"):
        print("Congratulation, You Win Brooo")
        youWin += 1
    elif (CIN == "Scissor" and youIn == "Paper"):
        print("Computer Win Brooo try again, Best Luckk!!")
        camWin += 1
    elif (CIN == "Rock" and youIn == "Scissor"):
        print("Computer Win Brooo try again, Best Luckk!!")
        camWin += 1
    elif (CIN == "Scissor" and youIn == "Rock"):
        print("Congratulation, You Win Brooo")
        youWin += 1
    elif (CIN == "Paper" and youIn == "Paper"):
        print("Its Tie Brooo")
        tie += 1
    elif (CIN == "Scissor" and youIn == "Scissor"):
        print("Its Tie Brooo")
        tie += 1
    elif (CIN == "Rock" and youIn == "Rock"):
        print("Its Tie Brooo")
        tie += 1
    turn -= 1

    if (turn == 0):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

        Exit = input("Do you want to play again? type Yes to play else type Exit: ")
        if (Exit == "Yes"):
            turn = int(input("Enter no of times you want to play: "))
        else:
            Exit == "Exit"
            break
print("Okk Byee!! Come again when You want to play😉 !!")
print("🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗")
print("****❤️ Final Result of the Game❤️ ****")
print("🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗")
print("Computer Score: ", camWin)
print("Your Score: ", youWin)
print("Number of Tie: ", tie)
print("🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗🤗")

if youWin > camWin:
    print("Hurray!!🥳 You Won with ", youWin, " point.")
elif youWin < camWin:
    print("Ohh no!!🥹 Computer Won with ", camWin, " point.")
else:
    print("Oops😕 It's a Tie!!")