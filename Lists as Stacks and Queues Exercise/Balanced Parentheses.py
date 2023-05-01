input_string = list(input())

list_2 = []
fail = False
for chr in input_string:
    if chr == "(" or chr == "{" or chr == "[":
        list_2.append(chr)
    else:
        if len(list_2) > 0:
            if chr == ")" and list_2[-1] == "(":
                list_2.pop()
            elif chr == "}" and list_2[-1] == "{":
                list_2.pop()
            elif chr == "]" and list_2[-1] == "[":
                list_2.pop()
            else:
                print("NO")
                fail = True
                break
        else:
            fail = True
            print("NO")
            break

if len(list_2) == 0 and fail == False:
    print("YES")
