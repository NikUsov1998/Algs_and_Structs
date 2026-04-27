def gnome_sort(seq: list) -> None:
    index: int = 1
    i: int = 0
    n: int = len(seq)
    while i < n-1:
        if seq[i] <= seq[i+1]:
            i, index = index, index + 1
        else:
            seq[i], seq[i + 1] = seq[i + 1], seq[i]
            i = i - 1
            if i < 0:
                i, index = index, index + 1