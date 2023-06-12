time = [int(num) for num in input().split(" ")]
number_of_tasks = [int(num) for num in input().split(" ")]
counter = {"Darth Vader Ducky": 0, "Thor Ducky": 0, "Big Blue Rubber Ducky": 0, "Small Yellow Rubber Ducky": 0}

while time and number_of_tasks:
    current_time = time.pop(0)
    current_number_of_tasks = number_of_tasks.pop()
    current_result = current_time * current_number_of_tasks
    if 0 <= current_result <= 60:
        counter["Darth Vader Ducky"] += 1
    elif 61 <= current_result <= 120:
        counter["Thor Ducky"] += 1
    elif 121 <= current_result <= 180:
        counter["Big Blue Rubber Ducky"] += 1
    elif 181 < current_result < 240:
        counter["Small Yellow Rubber Ducky"] += 1
    else:
        current_number_of_tasks -= 2
        number_of_tasks.append(current_number_of_tasks)
        time.append(current_time)

print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for key in counter.keys():
    print(f'{key}: {counter[key]}')
