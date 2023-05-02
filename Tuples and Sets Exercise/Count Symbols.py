input_word = input()
alphabet_dictionary = {}

for letter in input_word:
    if letter not in alphabet_dictionary.keys():
        alphabet_dictionary[letter] = 1
    else:
        alphabet_dictionary[letter] += 1

alphabet_dictionary = sorted(alphabet_dictionary.items(), key=lambda x: x[0])

for tuple in alphabet_dictionary:
    print(f'{tuple[0]}: {tuple[1]} time/s')
    
