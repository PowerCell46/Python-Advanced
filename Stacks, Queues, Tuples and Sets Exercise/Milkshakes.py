from collections import deque

chocolates = deque([int(num) for num in input().split(", ")][::-1])
cups_of_milk = deque([int(num) for num in input().split(", ")])
number_of_milkshakes = 0

while number_of_milkshakes < 5 and cups_of_milk and chocolates:
    current_chocolate = chocolates.popleft()
    current_cup_of_milk = cups_of_milk.popleft()
    if current_chocolate <= 0 and current_cup_of_milk <= 0:
        continue  # If both are invalid they are removed from the lists
    elif current_chocolate <= 0:
        cups_of_milk.appendleft(current_cup_of_milk)
        continue  # If the chocolate is invalid, append the milk to the end of the queue
    elif current_cup_of_milk <= 0:
        chocolates.appendleft(current_chocolate)
        continue  # If the milk is invalid, append the chocolate back to its place
    if current_chocolate == current_cup_of_milk:
        number_of_milkshakes += 1  # If the two values are equal, a shake is made and both products are removed
    else:  # If the values are different, we move the milk to the back of the queue and we decrease the chocolate by 5
        cups_of_milk.append(current_cup_of_milk)
        chocolates.appendleft(current_chocolate - 5)

if number_of_milkshakes == 5:
    print(f'Great! You made all the chocolate milkshakes needed!')
else:
    print(f'Not enough milkshakes.')
    
chocolates = [el for el in chocolates]
if len(chocolates) > 0:
    print(f'Chocolate: {", ".join([str(el) for el in chocolates][::-1])}')
else:
    print(f'Chocolate: empty')
    
if len(cups_of_milk) > 0:
    print(f'Milk: {", ".join([str(el) for el in cups_of_milk])}')
else:
    print(f'Milk: empty')
