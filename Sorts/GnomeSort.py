def gnome_sort(seq):
    index = 1
    i = 0
    n = len(seq)
    while i < n-1:
        if seq[i] <= list[i+1]:
            i, index = index, index + 1
        else:
            seq[i], list[i + 1] = list[i + 1], list[i]
            i = i - 1
            if i < 0:
                i, index = index, index + 1