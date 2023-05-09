rows, columns = [int(num) for num in input().split()]
word = input()
matrix = [["-" for el in range(columns)] for _ in range(rows)]
working_word = list(word)
for i in range(len(matrix)):
    row = matrix[i]
    if i % 2 != 0:
        if "".join(working_word) in word:
            working_word = working_word[::-1]
        for index in range(len(row) - 1, -1, -1):
            if len(working_word) > 0:
                matrix[i][index] = working_word.pop()
            else:
                working_word = list(word)[::-1]
                matrix[i][index] = working_word.pop()
    else:
        for index in range(len(row)):
            if "".join(working_word) not in word:
                working_word = working_word[::-1]
            if len(working_word) > 0:
                matrix[i][index] = working_word.pop(0)
            else:
                working_word = list(word)
                matrix[i][index] = working_word.pop(0)
                
    print("".join(row))
    
