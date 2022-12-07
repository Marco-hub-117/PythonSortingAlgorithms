def bubbleSort(list):
    n = len(list) - 1
    iteration = 0   # count the number of iteration, for demonstration purpose
    swapped = True
    while(swapped):
        swapped = False
        for i in range(0, n):
            iteration += 1
            if (list[i]>list[i+1]):
                swap(list, i)
                swapped = True
        n = n - 1 # Each time a for cycle end, we already have the greatest elements at the end of the list, so next time we don't need to compare those elements
        
    
    return iteration

def bubbleSortOptimized(list):
    # Possiamo affermare che ogni volta completato un ciclo for,
    # tutti gli elementi della lista da ordinare successivi all'ultimo
    # elemento scambiato siano già ordinati.
    # Questo perchè quando faccio il confronto
    # e questo mi restituisce che gli elementi sono già ordinati
    # quindi non mi serve niente rifare il confronto nella prossima iterazione del ciclo for per gli elementi successivi all'ultimo elemento scambiato nella precedente iterazione
    # ENG:
    # We can assume that at each "for" iteration 
    # every element after the last swapped element
    # is already ordered.
    # That because when the comparison happen
    # and that results in the elements that are already ordered
    # so the next for iteration can stop a the last swapped element in the previous iteration

    n = len(list) - 1
    lastSwapped = n
    iteration = 0   # count the number of iteration, for demonstration purpose
    swapped = True
    while(swapped):
        swapped = False
        for i in range(0, lastSwapped):
            iteration += 1
            if (list[i]>list[i+1]):
                lastSwapped = i
                swap(list, i)
                swapped = True
        
    
    return iteration

def swap(list, i):
    temp = list[i]
    list [i] = list [i+1]
    list[i+1] = temp

def main():
    numbers = [1,150,12,9,15,25,90,60,10,3,26,15,12,27,72,50,46,63,4,5,200,300,1000,1200,2000]
    print(numbers)

    iteration = bubbleSort(numbers)
    print(f'Number of iteration: {iteration}')
    print(numbers)

    numbers = [1,150,12,9,15,25,90,60,10,3,26,15,12,27,72,50,46,63,4,5,200,300,1000,1200,2000]
    iterationOptimized = bubbleSortOptimized(numbers)
    print(f'Number of iteration: {iterationOptimized}')
    print(numbers)



if __name__ == '__main__':
    main()
