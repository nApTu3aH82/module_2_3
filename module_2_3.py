my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count = 0
len_list = len(my_list)
while count <= len_list:
    if my_list[count] == 0:
        count += 1
        continue
    elif my_list[count] < 0:
        break
    else:
        print(my_list[count])
        count += 1
