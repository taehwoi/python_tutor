import random

TRIES = 10000 # number of tries
doors = ['goat'] * 3 # The three doors, with default values as 'goat'

# random integer among [0, 1, 2], which are index of the doors
car_position = random.randrange(0, 3)
doors[car_position] = 'car' # randomly place a car

win_count = 0 # total occurrence of winning a car, with swap strategy

for _ in range(TRIES):
    my_choice = random.randrange(0, 3) # randomly choose a door

    for door in range(len(doors)):
        # FILL ME IN (1):
        # from door among [0,1,2],
        # if the door has a goat, and not what I chose, host_choice = door
        if door != my_choice and door != car_position:
            host_choice = door
            break

    for door in range(len(doors)):
        # FILL ME IN (2):
        # Now that the host has shown me the door with a goat,
        # I will swap no matter what. In other words, 
        if door != my_choice and door != host_choice:
            changed_choice = door
            break

    # FILL ME IN (3):
    win_count += int(changed_choice == car_position)



print(win_count / TRIES * 100) # print the rate of winning
