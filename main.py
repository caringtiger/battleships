#!/bin/python
import random
gridsize_x = 5
gridsize_y = 5


def main():
    user_difficulty = get_user_difficulty()

    user_play_again = True
    # Game difficulty torpedo count. 0 = Easy, 1 = medium etc.
    game_difficulty_torpedos = [15,10,5,10]
    while user_play_again:
        game_map = init_game_map(gridsize_x,gridsize_y) #call the subroutine to set up the game
        # Set the total user torpedos based on the difficulty
        user_total_torpedos = game_difficulty_torpedos[user_difficulty]
        user_curr_torpedos = user_total_torpedos
        game_won = False

        print("Welcome to BattleShips!")
        print("An enemy ship is hidden somewhere at sea")
        print("We have no idea what a radar is so GEUSS!")
        print("you only have",user_total_torpedos," torpedoes to hit it.")

        while user_curr_torpedos > 0:
            print()
            draw_grid(game_map,gridsize_x,gridsize_y) #Call the subroutine to draw the current state of the game
            print()
            print("you have ", user_curr_torpedos, "torpedoes left")
            print("Enter the row and column seperatly to aim your torpedo.")

            user_target_x = int(input("Row?"))
            user_target_y = int(input("Column?"))
            if game_map[user_target_x][user_target_y] == "M":
                print("Holy fork you are dumb")

            elif game_map[user_target_x][user_target_y] == ".":
                game_map[user_target_x][user_target_y] = "M"

            elif game_map[user_target_x][user_target_y] == "S":
                game_map[user_target_x][user_target_y] = "X"
                game_won = True
                draw_grid(game_map,gridsize_x,gridsize_y)
                print("You won the game!")
                break
            user_curr_torpedos -= 1

        if game_won == True:
            print("You won the game with ", user_curr_torpedos, "out of ", user_total_torpedos, " torpedos left")
            score = user_curr_torpedos * game_difficulty_torpedos[user_difficulty]
            print(score)

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

def get_user_difficulty():
    while True:
        print("[1]. Easy")
        print("[2]. Medium")
        print("[3]. Hard")
        print("[4]. DEATH")
        # take's the user's desired difficulty as a string
        user_difficulty_str = input("Please enter 1,2,3 or 4: ")
        if user_difficulty_str == "1" or user_difficulty_str == "2" or user_difficulty_str == "3" or user_difficulty_str == "4":
            print("Correct Conditions")
            # Converts the string to an integer if it matches the variables
            return int(user_difficulty_str) - 1
            break
        else:
            print("stop it. get some help.")

# Basic Comparison Funciton
def compare(torpCount,listscore):
    if torpCount > listscore:
        return True
    else:
        return False

#Setup the game
def init_game_map(gridsize_x,gridsize_y):
    game_map = [["." for y in range(gridsize_y) ] for x in range(gridsize_x)]
    #Hide a ship at a random position

    game_ship_location_x = random.randrange(gridsize_x)
    game_ship_location_y = random.randrange(gridsize_y)
    print("shipx", game_ship_location_x, "shipY", game_ship_location_y)
    game_map[game_ship_location_x][game_ship_location_y] = "S"
    return game_map

#Draw Grid for other difficulties
def draw_grid(game_map,gridsize_x,gridsize_y):

    grid = "  "
    for x in range(gridsize_x - 1):
        grid = grid+str(x)+" "
    print(grid)
    for x in range(gridsize_x - 1):
        print(x, end=" ")
        for y in range(gridsize_y):
            if  game_map[x][y] == "S":
                 print(".", end=" ")
            if  game_map[x][y] == "M":
                print("M", end=" ")
            if  game_map[x][y] == "X":
                print("X", end=" ")
            if  game_map[x][y] == ".":
                print(".", end=" ")
        print()

main()
