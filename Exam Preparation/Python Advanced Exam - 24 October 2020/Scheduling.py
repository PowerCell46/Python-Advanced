jobs = [int(num) for num in input().split(", ")]
index = int(input())
cycles = 0

while True:
    current_min = min(jobs)
    current_index = jobs.index(current_min)
    cycles += current_min
    if current_index == index:
        break
    jobs[current_index] = 5000

print(cycles)
