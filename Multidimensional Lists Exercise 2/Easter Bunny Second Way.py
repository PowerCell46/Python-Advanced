rows = int(input())
matrix = [[el for el in input().split()] for _ in range(rows)]
bunny_coordinates = []
for i in range(0, len(matrix)):
    current_row = matrix[i]
    for index in range(0, len(current_row)):
        el = current_row[index]
        if el == "B":
            bunny_coordinates.append(i)
            bunny_coordinates.append(index)
        elif el != "X":
            matrix[i][index] = int(el)

sum_dict = {"up": None, "down": None, "left": None, "right": None}
positions_dict = {"up": [], "down": [], "left": [], "right": []}

for i in range(bunny_coordinates[1] + 1, len(matrix[0])):
    if matrix[bunny_coordinates[0]][i] != "X":
        if sum_dict["right"] == None:
            sum_dict["right"] = 0
        sum_dict["right"] += matrix[bunny_coordinates[0]][i]
        positions_dict["right"].append([bunny_coordinates[0], i])
    else:
        break
for i in range(bunny_coordinates[1] - 1, -1, -1):
    if matrix[bunny_coordinates[0]][i] != "X":
        if sum_dict["left"] == None:
            sum_dict["left"] = 0
        sum_dict["left"] += matrix[bunny_coordinates[0]][i]
        positions_dict["left"].append([bunny_coordinates[0], i])
    else:
        break
for i in range(bunny_coordinates[0] + 1, len(matrix)):
    if matrix[i][bunny_coordinates[1]] != "X":
        if sum_dict["down"] == None:
            sum_dict["down"] = 0
        sum_dict["down"] += matrix[i][bunny_coordinates[1]]
        positions_dict["down"].append([i, bunny_coordinates[1]])
    else:
        break
for i in range(bunny_coordinates[0] - 1, -1, -1):
    if matrix[i][bunny_coordinates[1]] != "X":
        if sum_dict["up"] == None:
            sum_dict["up"] = 0
        sum_dict["up"] += matrix[i][bunny_coordinates[1]]
        positions_dict["up"].append([i, bunny_coordinates[1]])
    else:
        break
results = [el for el in list(sum_dict.values()) if el != 0]
if results:
    if sum_dict["right"] == None:
        del sum_dict["right"]
    if sum_dict["left"] == None:
        del sum_dict["left"]
    if sum_dict["down"] == None:
        del sum_dict["down"]
    if sum_dict["up"] == None:
        del sum_dict['up']
    print(sorted(sum_dict.items(), key=lambda x: -x[1])[0][0])
    for f_list in (positions_dict[sorted(sum_dict.items(), key=lambda x: -x[1])[0][0]]):
        print(f_list)
    print(sorted(sum_dict.items(), key=lambda x: -x[1])[0][1])
