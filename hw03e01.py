# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    ndigits=int(ndigits)
    numlen=len(number)
    if ndigits<numlen : #убираем проблемные значения ndigits
        countpoint=0 #номер места точки или запятой
        for itm in range(len(number)):
            if number[itm] == "," or number[itm]==".":
                countpoint=int(itm)
        number=number[0:(countpoint)] + "." + number[(countpoint+1):numlen] #поправляю запятую
        if int(number[(countpoint+ndigits+1)])>4: # округляем математически
            number=str(float(number)+1/(10**ndigits))
        result = number[0:(countpoint+1+ndigits)]
    if ndigits>=numlen:
        result ='хотите слишком много знаков после запятой'
    return result

print(my_round(input('введите число для округления\n'), input('введите до скольки знаков округлить\n')))

