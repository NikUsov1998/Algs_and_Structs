def bubble_sort(seq):
    sorted_index = len(seq)
    while True:
        num_of_swap = 0
        for i in range(0, sorted_index-1):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                num_of_swap+=1
        sorted_index-=1
        if num_of_swap==0:
            break
