import pytest
from My_lessons.simpl_arif_oper import arithmetic


def test_arithmetic():
    assert arithmetic('2+3') == '5'
    assert arithmetic('5*5') == '25'
    assert arithmetic('5-5') == '0'
    assert arithmetic('4/2') == '2.00'
    assert arithmetic('500-5') == '495'
    assert arithmetic('5.6-1.6') == '4.00'
    assert arithmetic('2.2*1.2') == '2.64'
    assert arithmetic('3.6/2.1') == '1.71'
    assert arithmetic('2.4+6.5') == '8.90'
    assert arithmetic('852.98/8') == '106.62'
    # assert arithmetic('-5+5') == '0'
    assert arithmetic('5++6') == 'Неизвестная операция'
    assert arithmetic('') == 'Неизвестная операция'
    assert arithmetic('d/2') == 'Неизвестная операция'
    assert arithmetic('2f8') == 'Неизвестная операция'
    assert arithmetic('dfg') == 'Неизвестная операция'
    assert arithmetic('2/0') == 'ZeroDivisionError'
    assert arithmetic('2,2/2') == 'Запятая в числе, поставь точку!'


if __name__ == "__main__":
    pytest.main()
