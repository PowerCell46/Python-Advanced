price_for_a_bullet = int(input())
size_of_the_gun_barrel = int(input())
bullets = [int(number) for number in input().split(" ")]
locks = [int(number) for number in input().split(" ")]
value_of_the_intelligence = int(input())

current_barrel = size_of_the_gun_barrel

for i in range((len(bullets) - 1), -1, -1):
    current_bullet = bullets[i]
    if current_barrel == 0 and i + 1 < len(bullets):
        current_barrel = size_of_the_gun_barrel
        print(f'Reloading!')

    if len(locks) == 0:
        break
    for index in range(0, len(locks)):
        current_lock = locks[index]
        if current_bullet <= current_lock:
            print('Bang!')
            locks.pop(index)
        else:
            print("Ping!")
        bullets[i] = "$"
        break
    current_barrel -= 1

if len(locks) > 0:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f'{len([num for num in bullets if num != "$"])} bullets left. Earned ${value_of_the_intelligence - (price_for_a_bullet * bullets.count("$"))}')
