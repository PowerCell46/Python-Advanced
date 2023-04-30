quantity_of_food = int(input())
sequence_of_ints = [int(number) for number in input().split(" ")]
print(max(sequence_of_ints))
left_out_orders = []
index = 0
finished = False
while True:
    if index == len(sequence_of_ints):
        break
    order = sequence_of_ints[index]
    if quantity_of_food - order >= 0 and finished == False:
        sequence_of_ints.pop(0)
        quantity_of_food -= order
    else:
        finished = True
        left_out_orders.append(order)
        index += 1

if len(sequence_of_ints) == 0:
    print("Orders complete")
else:
    print(f'Orders left: {" ".join([str(num) for num in left_out_orders])}')
