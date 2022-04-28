from work_book.work_book_2.data_base import calk, minus

if __name__=="__main__":
    assert calk(4, 2) == 2
    assert calk(2, 0) == 'ZeroDivisionError'
    assert calk(2, 'f') == 'TypeError'
    assert calk(2, '!') == 'TypeError'
    assert calk('B', 'f') == 'TypeError'
    assert calk(4, 'dsfds') == 'TypeError'


    assert minus(4, 'g')=='TypeError'
    assert minus('D', 7)=='TypeError'
    assert minus('!', 0)=='TypeError'
    assert minus(3, -5)==8
    assert minus(-5, 2)==-7
    assert minus(-67, 0)==-67
    assert minus(0, 56)==-56