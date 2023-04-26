working_file = open("example.txt")
working_file_text = working_file.readlines()
number_of_the_line = 1
for line in working_file_text:
    letters_counter = 0
    punctuation_counter = 0
    for letter in line:
        if 64 < ord(letter) < 91 or 96 < ord(letter) < 123:
            letters_counter += 1
        if letter == "." or letter == "," or letter == "?" or letter == "!" or letter == "'" or letter == "-" or letter == '"' or letter == "(" or letter == ")" or letter == ";" or letter == ":" or letter == "`":
            punctuation_counter += 1
    if "\n" in line:
        line = list(line)
        line.pop()
        line = "".join(line)
    print(f'Line {number_of_the_line}: {line} ({letters_counter})({punctuation_counter})')
    number_of_the_line += 1
    
