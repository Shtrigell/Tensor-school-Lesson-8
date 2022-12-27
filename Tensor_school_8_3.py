import logging
def logs(func):
    """ Декоратор логирования.
    
    Функция записывает лог работы функции в файл my_log.log
    
    """
    def wrapper(*params):
        logging.basicConfig(filename="my_log.log", level=logging.DEBUG)
        logging.debug(f'Переданные параметры {params}')
        logging.info(f'Результат {sum(params)}')
        return func(*params)
    return wrapper
@logs
def summary(*args):
    """ Функция суммы.
    
    Функция для расчёта суммы чисел.
    Принимает неограниченное количество целочисленных значений - args.
    Возвращает целочисленное значение (сумму) - summ.
    
    """
    summ = 0
    for num in args:
        summ += num
    return summ
sum_list=[]
sum_list = input("Введите числа, через пробел, которые хотите сложить. Для выхода нахмите Enter. ").split()
for i in range (len(sum_list)):
    try:
        sum_list[i] = int(sum_list[i])
    except ValueError:
        print("Неверный формат данных, данные будут удалены.")
        sum_list[i] = 0
a=summary(*sum_list)
print("Ваша сумма: ", a)
