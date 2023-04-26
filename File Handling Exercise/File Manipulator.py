import os.path
import time

while True:
    current_command = str(input())
    if current_command == "End":
        break

    current_command = current_command.split("-")

    if current_command[0] == "Create":
        file_name = current_command[1]
        file = open(file_name, "w")
        file.write("")
        print(f'File "{file_name}" created/overwritten successfully!')
        file.close()
        time.sleep(0.5)

    elif current_command[0] == "Add":
        file_name = current_command[1]
        file = open(file_name, "a")
        file.write(current_command[2] + " \n")
        print(f'"{current_command[2]}" was successfully added to {file_name}!')
        file.close()
        time.sleep(0.5)

    elif current_command[0] == "Replace":
        file_name = current_command[1]
        if os.path.exists(file_name):
            file_text = open(file_name, "r")
            file_text = file_text.readlines()
            new_file = open(file_name, "w")
            new_file.write("")
            counter = 0
            for line in file_text:
                line = line.split(" ")
                final_line = []
                for word in line:
                    if word == current_command[2]:
                        final_line.append(current_command[3])
                        counter += 1
                    else:
                        final_line.append(word)
                new_file.write(" ".join(final_line))
                if counter > 0:
                    print(f'"{current_command[2]}" was successfully replaced with "{current_command[3]}" {counter} times!')
            new_file.close()
            time.sleep(0.5)
        else:
            print("An error occurred!")
            time.sleep(0.5)

    elif current_command[0] == "Delete":
        file_name = current_command[1]
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f'"{file_name}" was successfully deleted!')
            time.sleep(0.5)
        else:
            print("An error occurred!")
            time.sleep(0.5)

