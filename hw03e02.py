# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def luck(number):
    numlen=len(number)
    perpol=0
    vtorpol=0
    if numlen%2!=0:
        result="номер не четный"
    else:
        for i in range(numlen):
            if i<=numlen/2-1:
                perpol+=int(number[i])
            if i>numlen/2-1:
                vtorpol+=int(number[i])
        if perpol == vtorpol:
            result = 'счастливый'
        else: result = 'не счастливый'
    return result

print(luck(input('введите номер билета \n')))