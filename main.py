#!/bin/python
#battleships
import random
gridsize_x = 6
gridsize_y = 5
def main():
    print("line5")
    Difficulty = input("What Difficulty do you want? Easy, Medium,Hard OR And we highly reccomend this DEATH")
    if Difficulty == "DEATH":
        gridsize_x = 11
        gridsize_y = 10
    else:
        gridsize_x = 7
        gridsize_y = 6

    playAgain = "y"

    while playAgain == "y":
        sea = setupGame(gridsize_x,gridsize_y) #call the subroutine to set up the game
        if Difficulty == "Easy":
            torpCount =  15
        elif Difficulty == "Medium":
            torpCount = 10
        elif Difficulty == "Hard":
            torpCount = 5
        elif Difficulty == "DEATH":
            torpCount = 10

        gameWon = False

        print("Welcome to BattleShips!")
        print("An enemy ship is hidden somewhere at sea")
        print("We have no idea what a radar is so GEUSS!")
        print("you only have",torpCount," torpedoes to hit it.")

        while not gameWon and torpCount > 0:
            print()
            drawGrid(sea,gridsize_x,gridsize_y) #Call the subroutine to draw the current state of the game
            print()
            print("you have ", torpCount, "torpedoes left")
            print("Enter the row and column seperatly to aim your torpedo.")

            tryX = int(input("Row?"))
            tryY = int(input("Column?"))
            if sea[tryX][tryY] == "M":
                print("Holy fork you are dumb")

            else:
                if sea[tryX][tryY] == ".":
                    sea[tryX][tryY] = "M"

                if sea[tryX][tryY] == "S":
                    sea[tryX][tryY] = "X"
                    gameWon = True
            torpCount = torpCount - 1

        print()
        drawGrid(sea,gridsize_x,gridsize_y)
        print()

        if gameWon == True:
            if Difficulty == "Easy":
                torpCount = torpCount - 15
            elif Difficulty == "Medium":
                torpCount = torpCount - 10
            elif Difficulty == "Hard":
                torpCount = torpCount - 5
            elif Difficulty == "DEATH":
                torpCount = torpCount - 10
            print("WOW NICE JOB YOU LUCKY BICH YOU WON BUT YOU LOST US ", torpCount, "TORPEDO NICE JOB")
            print("TRY ANOTHER MODE IF YOU WANT")
            if Difficulty == "Easy":
                torpCount = torpCount + 15
            elif Difficulty == "Medium":
                torpCount = torpCount + 10
            elif Difficulty == "Hard":
                torpCount = torpCount + 5
            elif Difficulty == "DEATH":
                torpCount = torpCount + 10
            torpCount = newscore


            contents = []
            file = open("Highscorenumbers.txt","r")
            data = file.readline()
            file.close()
            data = data.replace(" ","")
            content = data.split(",")
            for num in content:
                contents.append(num)
            del contents[-1]
            print("Current List of HighScore\n")
            print(contents)
            for i in range(len(contents)):
                print(contents[i])

            open("Highscorenumbers.txt", 'w').close()

            firstplace = compare(torpCount(int(contents[0])))
            secondplace = compare(torpCount(int(contents[1])))
            thirdplace = compare(torpCount(int(contents[2])))
            fourthplace = compare(torpCount(int(contents[3])))
            print(contents)

            if firstplace == True:
                del contents[-1]
                contents.insert(0,torpCount)
                print("1st place\n {}".format(contents))
            elif secondplace == True:
                del contents[-1]
                contents.insert(1,torpCount)
                print("2nd place\n {}".format(contents))
            elif thirdplace == True:
                del contents[-1]
                contents.insert(2,torpCount)
                print("3rd place\n {}".format(contents))
            elif fourthplace == True:
                del contents[-1]
                contents.insert(3,torpCount)
                print("4th place\n {}".format(contents))
            else:
                print("Score did not make it onto the leader board")


            file = open("Highscorenumbers.txt","w")
            for i in range(len(contents)):
                file.write(str(contents[i])+",")
            file.close()

        else:
            print("YOU ARE USELESS YOU COULDNT EVEN FIGURE OUT HOW TO USE RADAR YOU JUST GEUSSED YOU IDIOT")
            print("TRY ANOTHER MODE IF YOU WANT")
            contents = []
            file = open("Highscorenumbers.txt","r")
            data = file.readline()
            file.close()
            data = data.replace(" ","")
            content = data.split(",")
            for num in content:
                contents.append(num)
            del contents[-1]
            print("Current List of HighScore\n")
            print(contents)
            for i in range(len(contents)):
                print(contents[i])

            open("Highscorenumbers.txt", 'w').close()

            firstplace = compare(torpCount(int(contents[0])))
            secondplace = compare(torpCount(int(contents[1])))
            thirdplace = compare(torpCount(int(contents[2])))
            fourthplace = compare(torpCount(int(contents[3])))
            print(contents)

            if firstplace == True:
                del contents[-1]
                contents.insert(0,torpCount)
                print("1st place\n {}".format(contents))
            elif secondplace == True:
                del contents[-1]
                contents.insert(1,torpCount)
                print("2nd place\n {}".format(contents))
            elif thirdplace == True:
                del contents[-1]
                contents.insert(2,torpCount)
                print("3rd place\n {}".format(contents))
            elif fourthplace == True:
                del contents[-1]
                contents.insert(3,torpCount)
                print("4th place\n {}".format(contents))
            else:
                print("Score did not make it onto the leader board")


            file = open("Highscorenumbers.txt","w")
            for i in range(len(contents)):
                file.write(str(contents[i])+",")
            file.close()

        print()
        playAgain = input("Do you want to fail I mean TRY again y/n?")

# Basic Comparison Funciton
def compare(torpCount,listscore):
    if torpCount > listscore:
        return True
    else:
        return False


# Draw Grid for DEATH Difficulty
def drawGridDEATH(sea,gridsize_x,gridsize_y):
    print(" 012345")
    
    for x in range(gridsize_x):
        print(x, end="  ")
        for y in range(gridsize_y):
            if  sea[x][y] == "S":
                print(".", end="")
            if  sea[x][y] == "M":
                print("M", end="")
            if  sea[x][y] == "X":
                print("X", end="")
            if  sea[x][y] == ".":
                print(".", end="")
        print()

#Setup the game
def setupGame(gridsize_x,gridsize_y):
    sea = [["." for y in range(gridsize_y) ] for x in range(gridsize_x)]
    #Hide a ship at a random position
    shipX = random.randrange(gridsize_x)
    shipY = random.randrange(gridsize_y)
    print("shipx", shipX, "shipY", shipY)
    sea[shipX][shipY] = "S"
    return sea

#Draw Grid for other difficulties
def drawGrid(sea,gridsize_x,gridsize_y):

    grid = "  "
    for x in range(gridsize_x - 1):
        grid = grid+str(x)+" "
    print(grid)
    for x in range(gridsize_x - 1):
        print(x, end=" ")
        for y in range(gridsize_y):
            if  sea[x][y] == "S":
                 print(".", end=" ")
            if  sea[x][y] == "M":
                print("M", end=" ")
            if  sea[x][y] == "X":
                print("X", end=" ")
            if  sea[x][y] == ".":
                print(".", end=" ")
        print()

main()
