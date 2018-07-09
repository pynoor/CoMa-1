# To focus a test: @pytest.mark.focus

import abstand
import pytest

# def test_get_value_from_file():
#     # Arrange
#     coordinates = (0, 0)
#     expected_result = "U"

#     # Act
#     result = abstand.get_value_from_file(coordinates)

#     # Assert
#     assert result == expected_result


# def test_get_another_value_from_file():
    # Arrange
    # coordinates = (0, 1)
    # expected_result = "P"

    # # Act
    # result = abstand.get_value_from_file(coordinates)

    # # Assert
    # assert result == expected_result


def test_first_sample():
    start = (0, 9)
    end = (2, 2)
    expected_result = 11

    result = abstand.abstand(start, end, "labyrinth.dat")
    print(result)
    assert result == expected_result


def test_second_sample():
    start = (0, 9)
    end = (0, 7)
    expected_result = -1

    result = abstand.abstand(start, end, "labyrinth.dat")

    assert result == expected_result


# def test_count_lines_in_file():
#     list_of_lines = abstand.get_lines_in_file("labyrinth.dat")
#     result = abstand.count_lines_in_file(list_of_lines)
#     expected_result = 4

#     assert result == expected_result


# def test_count_lines_in_file_with_default_filename():
#     list_of_lines = abstand.get_lines_in_file("labyrinth.dat")
#     result = abstand.count_lines_in_file(list_of_lines)
#     expected_result = 4

#     assert result == expected_result

# test what happens when start = end


def test_start_and_end_are_equal():
    start = (0, 1)
    end = (0, 1)
    expected_result = 0
    result = abstand.abstand(start, end, "labyrinth.dat")
    assert result == expected_result


def test_start_and_end_are_equal_labyrinth2():
    start = (0, 0)
    end = (0, 0)
    expected_result = 0
    result = abstand.abstand(start, end, "labyrinth2.dat")
    assert result == expected_result


def test_sample1_labyrinth3():
    start = (0, 0)
    end = (0, 2)
    expected_result = -1
    result = abstand.abstand(start, end, "labyrinth3.dat")
    assert result == expected_result


# def test_right_value_labyrinth3():
#     expected_result = "P"
#     result = abstand.get_value_from_file((0, 2), "labyrinth3.dat")

#     assert result == expected_result


def test_sample4_labyrinth4():
    start = (0, 0)
    end = (99,99)

    expected_result = -1
    result = abstand.abstand(start, end, "labyrinth4.dat")
    assert result == expected_result