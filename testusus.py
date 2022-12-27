import time
def sleep(func):
    '''Декоратор для функции подсчёт значения заданного элемента
    последовательности Фибоначчи, запрещающий вызов функции чаще
    чем раз в 5 секунд'''

    count = [0]
    last = [time.time()]

    def wrapper(n):
        # Первый вызов функции
        if count[0] == 0:
            count[0] += 1
            return func(n)
        # Последующие вызовы
        else:
            if time.time() - last[0] < 5:
                print(f'Слишком частый вызов функции. Результат будет выведен через {5 - (time.time() - last[0])} секунд')
                # Таймер
                time.sleep(5 - (time.time() - last[0]))
        count[0] += 1
        last[0] = time.time()
        return func(n)
    return wrapper


@sleep
def fibonacci(n):
    """ Функция Фибоначчи.
    
    Рекурсивная функция расчёта заданного числа Фибоначчи.
    Принимает целочисленное значение - порядковый номер эл-та в последовательности - n.
    Возвращает последовательность Фибоначчи до указаного элемента.
    
    """
    if (n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
try:
    n = int(input("Введите число членов последовательности:"))
except ValueError:
    print("Неверный формат данных")
else:
    print("Последовательность Фибоначчи:")
    for i in range(n):
        print(fibonacci(i))

