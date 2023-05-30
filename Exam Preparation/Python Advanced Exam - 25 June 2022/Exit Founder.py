first, second = input().split(", ")
matrix = [[el for el in input().split(" ")] for i in range(6)]
index = 0
hit_player = []

def move(coordinates, player):
    row = int(coordinates[1])
    position = int(coordinates[4])
    current_symbol = matrix[row][position]
    if current_symbol == "E":
        print(f'{player} found the Exit and wins the game!')
        return True
    elif current_symbol == "T":
        if player == "Tom":
            print(f'{player} is out of the game! The winner is Jerry.')
        else:
            print(f'{player} is out of the game! The winner is Tom.')
        return True
    elif current_symbol == "W":
        print(f'{player} hits a wall and needs to rest.')
        hit_player.append(player)


while True:
    if index % 2 == 0:
        current_player = first
    else:
        current_player = second
    current_coordinates = input()
    index += 1
    if len(hit_player) > 0 and current_player == hit_player[0]:
        search_index = hit_player.index(current_player)
        hit_player.pop(search_index)
    else:
        res = move(current_coordinates, current_player)
        if res:
            break
