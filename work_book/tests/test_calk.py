from work_book.work_book_2.data_base import calk, minus, plusse, cat

if __name__ == "__main__":
    assert calk(4, 2) == 2
    assert calk(2, 0) == 'ZeroDivisionError'
    assert calk(2, 'f') == 'TypeError'
    assert calk(2, '!') == 'TypeError'
    assert calk('B', 'f') == 'TypeError'
    assert calk(4, 'dsfds') == 'TypeError'

    assert minus(4, 'g') == 'TypeError'
    assert minus('D', 7) == 'TypeError'
    assert minus('!', 0) == 'TypeError'
    assert minus(3, -5) == 8
    assert minus(-5, 2) == -7
    assert minus(-67, 0) == -67
    assert minus(0, 56) == -56

    assert plusse(6, 'd') == 'TypeError'
    assert plusse('G', 5) == 'TypeError'
    assert plusse('G', 5) == 'TypeError'
    assert plusse(5, 0) == 5
    assert plusse(0, 10) == 10
    assert plusse(-6, 5) == -1
    assert plusse(-4, -2) == -6
    assert plusse(100, 52) == 152

    assert cat('dsfsd')=='мяу-мяу dsfsd'
    assert cat(2)== 'TypeError'
