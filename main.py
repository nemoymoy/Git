# Выполнение задания №2
from application.db.people import get_employees
from application.salary import calculate_salary
# Выполнение задания №3
import datetime
# Выполнение задания №4
from application.index_search import IndexSearch
import os


if __name__ == '__main__':
    print("---")

    print("Выполнение задания №1 и №2")
    calculate_salary()
    get_employees()
    print("---")

    print("Выполнение задания №3")
    print(datetime.datetime.now().strftime('%Y-%m-%d'))
    print(datetime.datetime.now().strftime('%H:%M:%S'))
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("---")

    print("Выполнение задания №4")
    # Считываем текст из 1-го файла
    with open('Hello.txt', 'r', encoding="utf-8") as f1:
        lines1 = f1.read()
    # Считываем текст из 2-го файла
    with open('Text.txt', 'r', encoding="utf-8") as f2:
        lines2 = f2.read()
    # Создаем экземпляр класса IndexSearch
    example_index = IndexSearch(os.getcwd())
    # Вызываем функцию создания Индекса из текста двух файлов, передавая в качестве аргументов две переменные с текстом
    example_index.create_index(lines1, lines2)
    # Вызываем функцию поиска текстовой подстроки в созданном Индексе
    example_index.search_index("море")
    print("---")
