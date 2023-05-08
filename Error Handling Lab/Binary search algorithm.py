import random
import time
from sty import ef, rs
import sty

list_length = random.randint(5, 100)
working_list = []
for i in range(list_length):
    working_list.append(random.randint(0, 1000))
print(f'This is the generated list:\n{working_list}')

try:
    searched_value = int(input(sty.fg(77) + "Enter a number that you wish to search for in the list: " + sty.fg(254)))
    if searched_value not in working_list:
        raise ValueError
except:
    searched_value = random.choice(working_list)
    time.sleep(0.5)
    print(sty.fg(160) + f'You have entered an invalid number, so the program chose a random one, which is: {ef.bold + str(searched_value) + rs.bold_dim + sty.fg(254)}')
    time.sleep(1)

counter = 0

while True:
    first_half = working_list[:len(working_list)//2]
    second_half = working_list[len(working_list)//2:]
    counter += 1
    if searched_value in first_half:
        working_list = first_half
    elif searched_value in second_half:
        working_list = second_half
    time.sleep(0.5)
    if len(working_list) == 1:
        print(f"Number {sty.fg(160) + ef.bold + str(searched_value) + rs.bold_dim + sty.fg(254)} was found on the {sty.fg(160) + ef.bold + str(counter) + rs.bold_dim + sty.fg(254)} turn.")
        break
    print(f'This is the list after it was cut in half: {working_list}')
