from collections import deque

bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(input().split())

total_honey = 0

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar < current_bee:
        bees.appendleft(current_bee)
    elif current_nectar > current_bee:
        total_honey += abs(operations[symbols.popleft()](current_bee, current_nectar))

print(f'Total honey made: {total_honey}')

if bees:
    print(f'Bees left: {", ".join([str(i) for i in bees])}')
if nectar:
    print(f'Nectar left: {", ".join([str(i) for i in nectar])}')
    
