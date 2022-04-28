from work_book.work_book_2.data_base import calk

if __name__=="__main__":
    assert calk(4, 2) == 2
    assert calk(2, 0) == 'ZeroDivisionError'
    assert calk(2, 'f') == 'TypeError'
    assert calk(2, '!') == 'TypeError'
    assert calk('B', 'f') == 'TypeError'
    assert calk(4, 'dsfds') == 'TypeError'