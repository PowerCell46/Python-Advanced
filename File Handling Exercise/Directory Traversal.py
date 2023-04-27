import os


def save_extensions(directory_name, first_level=False):
    for file in os.listdir(directory_name): #Въртим всички файлове в current folder-a
        file_1 = os.path.join(directory_name, file)

        if os.path.isfile(file_1):
            extension = file.split(".")[-1]
            if extension not in extensions:
                extensions[extension] = []
            extensions[extension].append(file)

        elif os.path.isdir(file_1):
            save_extensions(file_1, first_level=True)


directory = input()
extensions = {}
save_extensions(directory)
result = []

extensions = sorted(extensions.items(), key=lambda x: x[0])
for extension, files in extensions:
    result.append("."+ extension)
    for file in sorted(files):
        result.append(f'- - - {file}')

with open("report.txt", "w") as file:
    file.write("\n".join(result))
