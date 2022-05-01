import pytest
from My_lessons.square import square


def test_square():
    assert square('4') == (16.0, 16.0, 5.657)
    assert square('4.6') == (18.4, 21.16, 6.505)
    assert square('50') == (200, 2500, 70.711)
    assert square('004') == (16.0, 16.0, 5.657)
    assert square('5') == (20, 25, 7.071)
    assert square('0') == (0, 0, 0)
    assert square('-4') == 'Уберите минус'
    assert square('-4.6') == 'Уберите минус'
    assert square('d') == 'Неизвестная операция'
    assert square('36d') == 'Неизвестная операция'
    assert square('4,6') == 'Неизвестная операция'


if __name__ == "__main__":
    pytest.main()
