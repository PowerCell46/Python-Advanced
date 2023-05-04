import math


def primary_diagonal_recursion(index=0, elements=[]):
    if index < len(matrix):
        elements.append(matrix[index][index])
        index += 1
        return primary_diagonal_recursion(index, elements)
    else:
        return elements


def secondary_diagonal_recursion(index, elements=[], i=0):
    if index > -1 and i < len(matrix):
        elements.append(matrix[i][index])
        i += 1
        index -= 1
        return secondary_diagonal_recursion(index, elements, i)
    else:
        return elements


matrix = [[int(num) for num in input().split(" ")] for _ in range(int(input()))]
primary_elements = [num for num in primary_diagonal_recursion()]
secondary_elements = [num for num in secondary_diagonal_recursion(len(matrix)-1)]
print(math.trunc(math.fabs(sum(primary_elements) - sum(secondary_elements))))
