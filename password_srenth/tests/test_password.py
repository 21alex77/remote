'''
условия пароля, возвращает всегда строку:
1) если пароль короче 6 символов вернуть 'Пароль слишком короткий'
2) если пароль содержит только цифры, только буквы строчные, только буквы заглавные вернуть 'Пароль слабый'
3)если пароль содержит символы любых двух наборов вернуть 'Пароль хороший'
4) если пароль содержит символы всех трех наборов вернуть 'Пароль очень хороший'
'''


from password_srenth.password_analiz.analiz_funktion import analiz_password

if __name__=="__main__":
    assert analiz_password('12356')=='Пароль слишком короткий'
    assert analiz_password('dfg')=='Пароль слишком короткий'
    assert analiz_password('DFGFG')=='Пароль слишком короткий'
    assert analiz_password('erFG1')=='Пароль слишком короткий'
    assert analiz_password('123456')=='Пароль слабый'
    assert analiz_password('1234567')=='Пароль слабый'
    assert analiz_password('dfghjt')=='Пароль слабый'
    assert analiz_password('dfghjtyu')=='Пароль слабый'
    assert analiz_password('LKJHYU')=='Пароль слабый'
    assert analiz_password('FGDERTIDFSS')=='Пароль слабый'
    assert analiz_password('123ghj')=='Пароль хороший'
    assert analiz_password('ghjre12334')=='Пароль хороший'
    assert analiz_password('123GHJ')=='Пароль хороший'
    assert analiz_password('GHJL12334')=='Пароль хороший'
    assert analiz_password('fghGHJ')=='Пароль хороший'
    assert analiz_password('fghfdsfGHJFGF')=='Пароль хороший'
    assert analiz_password('12fgGH')=='Пароль очень хороший'
    assert analiz_password('fghGHJ123')=='Пароль очень хороший'
    assert analiz_password('fghf12df3GHfJ')=='Пароль очень хороший'

