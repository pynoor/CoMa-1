def quicksort(n, cmp, swp):
    '''
    This function sorts a list of n elements using the functions
    swp and cmp
    paramteres:
        - n = length(L)
        - cmp : a function that compares two elements
    '''
    if n <= 1:
        return 1

    if n == 2:
        if cmp(0,1):
            return 1
        else:
            swp(0,1)
            return 1

    def get_pivot_index(left):
        if not cmp(left, left+1):
            swp(left, left+1)
            if not cmp(left+1, left+2):
                swp(left+1, left+2)
                if not cmp(left, left+1):
                    swp(left, left+1)
        else:
            if not cmp(left+1, left+2):
                swp(left+1, left+2)
                if not cmp(left, left+1):
                    swp(left, left+1)
        return left+1

    def partition(pivot_index, left, right):
        swp(pivot_index, right)
        store_index = left
        for i in range(left, right):
            if cmp(i, right):
                swp(store_index, i)
                store_index += 1
        swp(right, store_index)
        return store_index

    def quicksortrecursion(left, right, cmp, swp):
        if right-left <= 0:
            return
        if right-left == 1:
            if cmp(left, right):
                return
            else:
                swp(left, right)
                return
        pivot_index = get_pivot_index(left)
        pivot_index = partition(pivot_index, left, right)
        quicksortrecursion(left, pivot_index -1, cmp, swp)
        quicksortrecursion(pivot_index+1, right, cmp, swp)
        return

    quicksortrecursion(0, n-1, cmp, swp)

    return 1
