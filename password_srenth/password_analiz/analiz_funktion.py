import string

'''
условия пароля, возвращает всегда строку:
1) если пароль короче 6 символов вернуть 'Пароль слишком короткий'
2) если пароль содержит только цифры, только буквы строчные, только буквы заглавные вернуть 'Пароль слабый'
3)если пароль содержит символы любых двух наборов вернуть 'Пароль хороший'
4) если пароль содержит символы всех трех наборов вернуть 'Пароль очень хороший'
'''

def analiz_password(password: any) -> str:
    if len(password) < 6:
        return 'Пароль слишком короткий'
    digits = string.digits
    letter = string.ascii_lowercase
    letter_big = letter.upper()
    caunt=0
    for symbol in (digits, letter, letter_big):
        if any(e in symbol for e in password):
            caunt+=1
            continue
    if caunt==3:
        return 'Пароль очень хороший'
    return 'Пароль слабый' if caunt==1 else 'Пароль хороший'


# if __name__ == "__main__":
#     analiz_password(password)
