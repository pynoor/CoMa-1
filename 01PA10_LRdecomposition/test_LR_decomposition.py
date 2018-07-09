import pytest
import LR_decomposition

def test_first_instance():
    result = LR_decomposition.LR_decomposition('2 4 -7, -4 -7 13, 34 71 -131')
    expected_result = '2 4 -7, -2 1 -1, 17 3 -9'
    assert result == expected_result

def test_second_instance():
    result = LR_decomposition.LR_decomposition('7 3 -1 2, 3 8 1 -4, -1 1 4 -1, 2 -4 -1 6')
    expected_result = '7 3 -1 2, 0 6 1 -4, 0 0 3 0, 0 0 0 1'
    assert result == expected_result

def test_fourth_instance():
    result = '5 -3, 7 -8'
    expected_result = LR_decomposition.LR_decomposition('5 -3, 35 -29')
    assert result == expected_result

def test_fifth_instance():
    result = '17 4, -1 46'
    expected_result = LR_decomposition.LR_decomposition('17 4, -17 42')
    assert result == expected_result

def test_sixth_instance():
    result = '-1 -7 4, 6 10 -2, -9 -6 -9'
    expected_result = LR_decomposition.LR_decomposition('-1 -7 4, -6 -32 22, 9 3 -33')
    assert result == expected_result
