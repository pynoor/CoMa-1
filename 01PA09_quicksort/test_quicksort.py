import pytest
import quicksort

L = ["Gode", "Goethe", "Goldmann", "Göbel", "Götz"]
A = [6,3,8,2,7,1,4,5]
B = [4,2,11,1,13,6,7,14,8,3,10,9,12,5]

def swp(i, j):
    global L
    L[i], L[j] = L[j], L[i]

def dinoswp_A(i, j):
    global A
    A[i], A[j] = A[j], A[i]

def dinoswp_B(i, j):
    global B
    B[i], B[j] = B[j], B[i]


def cmp_din5007a(i, j):
    a = L[i].casefold().replace('ä', 'a').replace('ö', 'o').replace('ü', 'u')
    b = L[j].casefold().replace('ä', 'a').replace('ö', 'o').replace('ü', 'u')
    return a <= b

def cmp_din5007b(i, j):
    a = L[i].casefold().replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')
    b = L[j].casefold().replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')
    return a <= b

def cmp_dinosample1(i, j):
    a = A[i]
    b = A[j]
    return a <= b

def cmp_dinosample2(i, j):
    a = B[i]
    b = B[j]
    return a <= b

def test_first_instance():
    expected_result = 1
    result = quicksort.quicksort(5, cmp_din5007a, swp)
    print(L)
    assert result == expected_result

def test_second_instance():
    expected_result = 1
    result = quicksort.quicksort(5, cmp_din5007b, swp)
    print(L)
    assert result == expected_result

def test_dinosample1():
    expected_result = 1
    result = quicksort.quicksort(8, cmp_dinosample1, dinoswp_A)
    print(A)
    assert result == expected_result

def test_dinosample2():
    expected_result = 1
    result = quicksort.quicksort(14, cmp_dinosample2, dinoswp_B)
    print(B)
    assert result == expected_result
