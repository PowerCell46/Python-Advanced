import re
text = re.split(r"[ ]{0,}[|]{1}[ ]{0,1}", input())
result = []
for row in range(len(text) - 1, -1, -1):
    row = text[row].split(" ")
    row = [x for x in row if x]  # remove empty strings
    result.extend(row)
print(" ".join(result))
