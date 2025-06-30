import os
import datetime
from functools import wraps

def logger(path):


    def __logger(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            start = datetime.datetime.now()
            result = old_function(*args, **kwargs)

            args_foo = [item for item in args]
            kwargs_foo = [f'{key} {value}' for key, value in kwargs.items()]

            log_string = (f"Дата и время запуска функции: {start}\n"
                          f"Имя функции: {old_function.__name__}\n"
                          f"Аргументы функции: {args_foo} {kwargs_foo}\n"
                          f"Результат функции: {result}\n")

            print(log_string)

            with open(path, 'a') as f:
                f.write(log_string)

            return result

        return new_function

    return __logger

path = 'my_test.log'
if os.path.exists(path):
    os.remove(path)

list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

@logger(path)
def flat_generator(list_of_list):
    for list_ in list_of_list:
        if isinstance(list_, list):
            yield from flat_generator(list_)
        else:
            yield list_

if __name__ == '__main__':
    flat_generator(list_of_lists_2)