file = open("example.txt")
file_info = file.readlines()
index = 0
for row in file_info:
    if index % 2 == 0:
        current_final_sentence = []
        for letter in row:
            if letter == "-" or letter == "," or letter == "." or letter == "!" or letter == "!" or letter == "?":
                current_final_sentence.append("@")
            else:
                current_final_sentence.append(letter)
        current_final_sentence = "".join(current_final_sentence)
        current_final_sentence = current_final_sentence.split(" ")
        final_current_sentence = []
        for i in range(len(current_final_sentence) -1, -1, -1):
            current_word = current_final_sentence[i]
            if "\n" in current_word:
                current_word = [letter for letter in current_word]
                current_word.pop()
                current_word = ''.join(current_word)
            final_current_sentence.append(current_word)
        print(" ".join(final_current_sentence))
    index += 1
