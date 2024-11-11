def GnomeSort(list):
    index = 1
    i = 0
    n = len(list)
    while i < n-1:
        if list[i] <= list[i+1]:
            i, index = index, index + 1
        else:
            list[i], list[i + 1] = list[i + 1], list[i]
            i = i - 1
            if i < 0:
                i, index = index, index + 1