class ValueCannotBeNegative(Exception):
    """There can only be positive numbers"""


for _ in range(0, 5):
    if int(input()) < 0:
        raise ValueCannotBeNegative
    else:
        print('Valid number.')
