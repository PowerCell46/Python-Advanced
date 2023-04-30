kids_list = input().split(" ")
nth_toss = int(input())

index = 0
current_toss = 0

while len(kids_list) > 1:
    current_child = kids_list[index]

    current_toss += 1

    if current_toss == nth_toss:
        print(f'Removed {kids_list.pop(index)}') # Не инкрементираме индекса, защото намаляваме дължината с единица, иначе ще скипнем един елемент.
        current_toss = 0
    else:
        index += 1
    if index == len(kids_list):
        index = 0

if len(kids_list) == 1:
    print(f'Last is {kids_list[0]}')

