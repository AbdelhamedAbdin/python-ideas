def Max():
    arr = [1, 3, 4, 2]
    i = 1
    max_num = 0

    for x in arr:
        arr_length = len(arr) - 1
        if i > arr_length:
            break
        elif x > arr[i]:
            max_num = x
            i += 1
        else:
            max_num = arr[i]
    return max_num

print(Max())