def merge(seq, support, ls, le, rs, re):
    for i in range(ls, re+1):
        support[i] = seq[i]
    l = ls
    r = rs
    for i in range(ls, re+1):
        if l > le:
            seq[i] = support[r]
            r+=1
        elif r > re:
            seq[i] = support[l]
            l+=1
        elif support[l] < support[r]:
            seq[i] = support[l]
            l+=1
        else:
            seq[i] = support[r]
            r+=1


def merge_sort(seq, support=None, start_index=None, stop_index=None):
    if support is None:
        support=seq[::]
    if stop_index is None:
        start_index = 0
    if stop_index is None:
        stop_index = len(seq) - 1
    if stop_index <= start_index:
        return None
    h = start_index + (stop_index-start_index)//2
    merge_sort(seq, support, start_index, h)
    merge_sort(seq, support, h+1, stop_index)
    merge(seq, support, start_index, h, h+1, stop_index)
