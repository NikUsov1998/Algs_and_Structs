def BubbleSort(list):
    sorted_index = len(list)
    while True:
        numberOfSwap = 0
        for i in range(0, sorted_index-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                numberOfSwap+=1
        sorted_index-=1
        if numberOfSwap==0:
            break
