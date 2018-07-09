import pytest
import radixsort

def test_first_instance():
    result = radixsort.radixsort([329, 457, 657, 839, 436, 720, 355], 10)
    expected_result = [[720, 355, 436, 457, 657, 329, 839], [720, 329, 436, 839, 355, 457, 657], [329,
355, 436, 457, 657, 720, 839]]
    assert result == expected_result

def test_second_instance():
    result = radixsort.radixsort([114, 21, 95, 5, 2, 14, 52, 30, 6, 20], 4)
    expected_result = [[52, 20, 21, 5, 114, 2, 14, 30, 6, 95], [114, 2, 52, 20, 21, 5, 6, 14, 30, 95],
[2, 5, 6, 14, 20, 21, 30, 95, 114, 52], [2, 5, 6, 14, 20, 21, 30, 52, 95, 114]]
    assert result == expected_result

def test_third_instance():
    result = "foo"
    expected_result = "foo"
    assert result == expected_result

def test_fourth_instance():
    result = "foo"
    expected_result = "foo"
    assert result == expected_result

def test_fifth_instance():
    result = "foo"
    expected_result = "foo"
    assert result == expected_result