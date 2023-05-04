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


matrix = [[int(num) for num in input().split(", ")] for _ in range(int(input()))]
primary_elements = [str(num) for num in primary_diagonal_recursion()]
print(f'Primary diagonal: {", ".join(primary_elements)}. Sum: {sum([int(num) for num in primary_elements])}')
secondary_elements = [str(num) for num in secondary_diagonal_recursion(len(matrix)-1)]
print(f'Secondary diagonal: {", ".join(secondary_elements)}. Sum: {sum([int(num) for num in secondary_elements])}')
