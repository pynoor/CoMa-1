import pytest
import auswertung

def test_first_word ():
    expected_result = (True , 0)
    result = auswertung.auswertung("!!x0|x1&x2", [True, True, False])
    assert result == expected_result

def test_second_word ():
    expected_result = (False , 1 )
    result = auswertung.auswertung("(!!x0|x1)&x2", [True, True, False])
    assert result == expected_result

def test_third_word ():
    expected_result = (True , 3)
    result = auswertung.auswertung("!([!x0]|[[x1]&x2])", [True, True, False])
    assert result == expected_result

def test_fourth_word ():
    expected_result = (True , 0)
    result = auswertung.auswertung("x0|!x0", [True])
    assert result == expected_result

def test_fifth_word():
    with pytest.raises(Exception) as excinfo:
        auswertung.auswertung("x0x1", [True, True])
    assert str(excinfo.value) == "Unzulaessiger Satzbuchstabenindex: ..."

def test_sixth_word():
    with pytest.raises(Exception) as excinfo:
        auswertung.auswertung("(x0|x1]", [False, False])
    assert str(excinfo.value) == "Unzulaessige Formel: Klammern passen nicht zusammen: ] gefunden; ) erwartet."

def test_seventh_word():
    with pytest.raises(Exception) as excinfo:
        auswertung.auswertung("x0!|x1", [True, False])
    assert str(excinfo.value) == "Unzulaessiger Satzbuchstabenindex: ..."

def test_eight_word():
    expected_result = (False, 3)
    result = auswertung.auswertung("[x4]|[x1]&((x0&x4|(x1))|x0&x0|x1)&x0", [True, False, True, False, False])
    assert result == expected_result