word = input()
repeating_times = input()
try:
    print(word * int(repeating_times))
except:
    raise TypeError("Variable times must be integer")
#    print("Variable times must be integer")
