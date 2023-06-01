def best_list_pureness(list_of_numbers, number_k):
    biggest_pureness = 0
    biggest_pureness_index = 0
    for i in range(len(list_of_numbers)):
        biggest_pureness += i * list_of_numbers[i]
    index = 0
    while number_k > 0:
        number_k -= 1
        el = list_of_numbers.pop()
        list_of_numbers.insert(0, el)
        current_pureness = 0
        index += 1
        for i in range(len(list_of_numbers)):
            current_pureness += i * list_of_numbers[i]
        if current_pureness > biggest_pureness:
            biggest_pureness = current_pureness
            biggest_pureness_index = index
    return (f'Best pureness {biggest_pureness} after {biggest_pureness_index} rotations')
