#1. Дан словарь, в котором ключами являются имена студентов, а значениями их оценки. По данному словарю, составить новый словарь, в котором ключами являются оценки, а значениями списки студентов, которые получили данную оценку.
#
#2. Дана строка, представляющая собой целое положительное число, записанное римскими цифрами. Написать функцию, возвращающую десятичное представление данного числа арабскими цифрами. 
#
#3. (дополнительная задача, со звездочкой) По целому положительному числу, записанному арабскими цифрами, получить его представление римскими цифрами. 



########################



D = {"Василий":5, "Анна":5, "Петр":4, "Сергей":4, "Мария":3, "Иван":2, "Ярослав":5}
new_D = {}


for key in D:
    if D[key] in new_D:
        new_D[D[key]].extend([key])
    else:
        new_D.update({D[key]:[key]})
        
print(new_D)
        
# new_D = {5: ['Василий', 'Анна', 'Ярослав'], 4: ['Петр', 'Сергей'], 3: ['Мария'], 2: ['Иван']}



########################



def number(string):
    dictionary = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    mas = list(string)
    for i in range(len(mas)):
        mas[i] = dictionary[mas[i]]   
    it = 0
    mas.append(0)
    summary = 0 
    while it != (len(mas)-1):
        if mas[it] >= mas[it+1]:
            summary += mas[it]
            it += 1
        else:
            summary += (mas[it+1]-mas[it])
            it += 2
    return(summary)

print(number('MCMXCIX'))



########################