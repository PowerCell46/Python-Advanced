def palindrome(word, index, reverse_word="", first_time=True):
    if index == 0 and first_time:
        index = (len(word) - 1)
        first_time = False
    if index > -1:
        reverse_word += word[index]
        index -= 1
        return palindrome(word, index, reverse_word, first_time=False)
    elif index == -1:
        if reverse_word == word:
            return f'{reverse_word} is a palindrome'
        else:
            return f'{word} is not a palindrome'
