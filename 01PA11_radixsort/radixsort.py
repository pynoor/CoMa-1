import math
def posnumsys(x, k):
    '''
    Transforms an number x in base 10 into a number in base k
    '''
    restlist  = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G",
     "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
     "V", "W", "X", "Y", "Z"]
    output = []
    while x > 1:
        rest = x % k
        output.append(restlist[rest])
        if rest != 0:
            x = (x - rest) // k
        else:
            x = x // k
    output.append(str(x))
    output.reverse()
    output = "".join(output)
    return output

def lastdig(x, i):
    '''
    This function returns the last i-th digit of a number x
    '''
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G",
     "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
     "V", "W", "X", "Y", "Z"]
    x = list(x)
    if x[-i].isdigit():
        return int(x[-i])
    else:
        return numbers.index(x[-i])



def radixsort(A, k):
    '''
    This function sorts a given list A in terms of the k-numeral system
    representation of its elements.

    Parameters:
        - List of integers A
        - Base k
    '''
    if len(A) <= 1:
        return A

    store_A = A
    A = [posnumsys(x, k) for x in A]
    d = max([len(x) for x in A])
    d_2 = math.floor(math.log(max(store_A), k))
    A = [x.zfill(d) for x in A]
    Dict = {}

    for index in range(len(A)):
        Dict[A[index]] = store_A[index]

    output = []
    for i in range(1, d_2+2):
        A = sorted(A, key= lambda x: lastdig(x, i))
        output.append(A)

    output = [[Dict[number] for number in sublist] for sublist in output]
    return output

