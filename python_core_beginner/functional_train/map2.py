# В списке содержатся строки с числами. Эти строки содержат ошибки: лишние пробелы, неправильные разделители целой и десятичной части и тд.
#Создайте функцию, которая сначала исправит ошибки в строках, а затем преобразует каждую строку в вещественное число. 

digits = ["12", "145", "  45", "12.4", "45,14", "15 645"]

def normal(element):
    element = element.replace(' ','').replace(',','.')
    return element

right_digits = map(float,map(normal,digits))

print(*right_digits)