"""Snake, Water and Gun Game
snake drinks water therefore the snake wins
Water absorbs the gun and gun goes haywire therefore the water wins
gun can shoot a snake therefore the gun wins
the game will be played 10 times out of which who gets the maximum score will win the game"""

import random
options = ["s","w","g"]
print("Welcome to the Snake, Water and Gun Game")
humanpoints = 0
computerpoints = 0
chance = 0
noofchance = 0
print("Type\n s for snake\nw for water\ng or gun\n")

while noofchance < 10:
    userinput = input("\t\nsnake,Water or Gun :-  ")
    computerinput = random.choice(options)

    if userinput == computerinput:
        print("#Tied by both .Because both choose same thing And no point given to anyone")
        print("#Your point is", humanpoints)
        print("#Computer point is", computerpoints)
        noofrounds = noofchance+ 1

    else:
        print("")

    if userinput=="s" and computerinput=="w":
        print("Snake drank the water\nAnd 1 point added in side of human")
        humanpoints=humanpoints+1
        print("#Your point is",humanpoints)
        print("#Computer point is", computerpoints)
        noofchance = noofchance + 1

    elif userinput=="s" and computerinput=="g":
        print("Snake killed by Gun\n And 1 point added in side of Computer")
        computerpoints=computerpoints+1
        print("#Your point is", humanpoints)
        print("#Computer point is", computerpoints)
        noofchance = noofchance + 1

    elif userinput == "w" and computerinput == "g":
        print("snkae killed by gun\n and 1 point is added to computer points")
        computerpoints = computerpoints +1
        print("your point is ", humanpoints)
        print("your point is ",computerpoints)
        noofchance = noofchance +1

    elif userinput=="w" and computerinput=="s":
        print("Snake drank the water And 1 point added in side of Computer")
        computerpoints=computerpoints+1
        print("#Your point is", humanpoints)
        print("#Computer point is",computerpoints)
        noofchance = noofchance + 1

    elif userinput=="g" and computerinput=="s":
        print("Gun killed the Snake And 1 point added in side of human")
        humanpoints=humanpoints+1
        print("#Your point is", humanpoints)
        print("#Computer point is", computerpoints)
        noofchance = noofchance + 1

    elif userinput=="g" and computerinput=="w":
         print("Water Screwed up the Gun And 1 point added in side of Computer")
         computerpoints=computerpoints+1
         print("#Your point is",humanpoints)
         print("#Computer point is", computerpoints)
         noofchance = noofchance + 1

    else:
        print("")
    print(computerpoints)
    print(humanpoints)
if humanpoints>computerpoints:
    print("Human points are more than Computer .So Human wins")
if humanpoints < computerpoints:
    print("Computer points is more than Human points .So Computer wins")
    print("Your point is", humanpoints, "And computer points is", computerpoints)

if noofchance == chance:
    print("GAME OVER ^_~")
    if noofchance==10:
        quit()




