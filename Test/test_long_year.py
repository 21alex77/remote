import pytest
from My_lessons.long_year import long_years

def tests_long_year():
    assert long_years('2022')=='Обычный год'
    assert long_years('2021')=='Обычный год'
    assert long_years('2023')=='Обычный год'
    assert long_years('1996')=='Високостный год'
    assert long_years('2028')=='Високостный год'
    assert long_years('1848')=='Високостный год'
    assert long_years('1964')=='Високостный год'
    assert long_years('2000')=='Високостный год'
    assert long_years('0')=='нет данных'
    assert long_years('-562')=='нет данных'
    assert long_years('2100')=='Обычный год'
    assert long_years('fsd')=='Неизвестная операция'
    assert long_years('sf25')=='Неизвестная операция'
    assert long_years('20-2')=='Неизвестная операция'
    assert long_years('0.5')=='Неизвестная операция'

if __name__=="__main__":
    pytest.main()