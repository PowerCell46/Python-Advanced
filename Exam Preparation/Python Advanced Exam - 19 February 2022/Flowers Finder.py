vowels = [letter for letter in input().split(" ")]
consonants = [letter for letter in input().split(" ")]
lst = ["rose", "tulip", "lotus", "daffodil"]
words = ["r", "o", "s", "e"], ["t", "u", "l", "i", "p"], ["l", "o", "t", "u", "s"], ["d", "a", "f", "f", "o", "d", "i", "l"]
while vowels and consonants:
    current_vowel = vowels.pop(0)
    current_consonant = consonants.pop()
    for i in range(len(lst)):
        if current_consonant in lst[i]:
            lst[i] = lst[i].replace(current_consonant, "")
        if current_vowel in lst[i]:
             lst[i] = lst[i].replace(current_vowel, "")
    if "" in lst:
        search_index = lst.index("")
        print(f'Word found: {"".join(words[search_index])}')
        break

if "" not in lst:
    print(f'Cannot find any word!')

if vowels:
    print(f'Vowels left: {" ".join(vowels)}')
if consonants:
    print(f'Consonants left: {" ".join(consonants)}')
