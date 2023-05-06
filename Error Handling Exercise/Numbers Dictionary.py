numbers_dictionary = {}

line = input("Enter a name for the value: ")

while line != "Search":
    number_as_string = line
    try:
        number = int(input("Enter a number for that name(Search-exit): "))
        numbers_dictionary[number_as_string] = number
    except:
        print(f'The variable number must be an integer')
    line = input("Enter a name for the value: ")

line = input("Enter name of a number that you wish to search for(Remove-exit): ")

while line != "Remove":
    searched = line
    try:
        print(numbers_dictionary[searched])
    except:
        print(f'Number does not exist in dictionary')
    line = input("Enter name of a number that you wish to search for(Remove-exit): ")

line = input("Enter name of a number that you wish to delete from the dictionary(End-exit): ")

while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except:
        print(f'Number does not exist in dictionary')
    line = input("Enter name of a number that you wish to delete from the dictionary(End-exit): ")

print(numbers_dictionary)
