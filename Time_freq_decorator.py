import time

def timer(func):
    """ Декоратор таймера.
    
    Функция выводит на экран время выполнения функции.
    
    """
    def wrapper(n):
        start = time.time()
        func(n)
        stop = time.time()
        print(f'Время выполнения функции:', stop - start)
        return func
    return wrapper

@timer
def print_fib(n):
    def fibonacci(n):
        if n in (1, 2):
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)
    print(f'Значение элемента последовательности Фибоначчи с порядковым номером {n} равно {fibonacci(n)}')

try:
    n = int(input("Введите порядковый номер элемента последовательности Фибоначчи: "))
except:
    print('Порядковый номер элемента последовательности Фибоначчи должен быть целым положительным числом')
    exit()
if n < 0:
    print('Порядковый номер элемента последовательности Фибоначчи должен быть целым положительным числом')
    exit()

print_fib(n)