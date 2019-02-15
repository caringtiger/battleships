#!/bin/python
import random
gridsize_x = 5
gridsize_y = 5

# Game difficulty torpedo count. 0 = Easy, 1 = medium etc.
game_difficulty_torpedos = [15,10,5,10]

def main():
    user_difficulty = get_user_difficulty()

    user_play_again = True
    while user_play_again == True:
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
            save_game(score)
        else:
            print("YOU ARE USELESS YOU COULDNT EVEN FIGURE OUT HOW TO USE RADAR YOU JUST GEUSSED YOU IDIOT")
            print("TRY ANOTHER MODE IF YOU WANT")


        user_difficulty_str = input("Do you want to play again? (y/n)")
        if user_difficulty_str.lower() == "n":
            print("Thank you for playing!")
            exit()


def save_game(score):
    with open('highscore.txt', 'r') as read_file:
        file_buffer = [int(x) for x in read_file.read().splitlines()]
        file_buffer.append(score)
        file_buffer.sort()
        with open('highscore.txt', 'w') as write_file:
            write_file.write('\n'.join(str(line) for line in file_buffer))

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
