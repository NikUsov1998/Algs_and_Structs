def select_sort(seq):
    for i in range(0, (len(seq)-1)):
        min_index = i
        for j in range(i+1, len(seq)):
            if seq[min_index] > seq[j]:
                min_index = j
            if min_index != i:
                temp = seq[i]
                seq[i] = seq[min_index]
                seq[min_index] = temp
