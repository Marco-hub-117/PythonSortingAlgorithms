# The logic is simple, we start from the leftmost element and keep track of the index of smaller (or equal to) elements as i. 
# While traversing, if we find a smaller element, we swap the current element with arr[i]. Otherwise, we ignore the current element. 

def quickSort(list, low, high):
    pivotIndex = high
    i = low - 1
    pivot = list[pivotIndex]
    if(low < high):
        for j in range (low, high):
            if (list[j] < pivot):
                i += 1
                (list[i], list[j]) = (list[j], list[i])

        (list[i+1], list[pivotIndex]) = (list[pivotIndex], list[i+1])
        quickSort(list, low, i)
        quickSort(list, i+1, high)
    

def main():
    numbers = [1,3,150,2,6,12,9,15,25,90,60,10]
    print(numbers)

    quickSort(numbers, 0, len(numbers) - 1)
    print(numbers)




if __name__ == '__main__':
    main()