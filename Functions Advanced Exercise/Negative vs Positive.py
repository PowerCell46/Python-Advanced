import math

list_of_numbers = input().split(" ")
list_of_numbers = [int(number) for number in list_of_numbers]


def sum_of_positive_negative(list_of_nums):
    negative_sum = 0
    positive_sum = 0
    for num in list_of_nums:
        if num < 0:
            negative_sum += num
        else:
            positive_sum += num
    result = f'{negative_sum}\n{positive_sum}\n'
    if math.fabs(negative_sum) > positive_sum:
        print(result + f'The negatives are stronger than the positives')
    elif positive_sum > math.fabs(negative_sum):
        print(result + f'The positives are stronger than the negatives')


sum_of_positive_negative(list_of_numbers)
