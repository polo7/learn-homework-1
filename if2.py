"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    # Решал задачу, исходя из того, что условия перебора идут в нисходящем порядке приоритета.
    # Иначе условиями не определено поведение, когда первая строяка длиннее, но вторая - learn.
    #
    # Также в условиях не рассмотрены случаи, когда 
    # а) строки разные и одинаковой длины
    # б) строки разные и вторная длиннее
    # В этих случаях возвращает -1, ведь функция должна что-то вернуть.
    def str_compare(str1, str2):
      if not (type(str1) == str and type(str2) == str):
        return 0
      elif str1 == str2:
        return 1
      elif len(str1) > len(str2):
        return 2
      elif str2 == 'learn':
        return 3
      else:
        return -1
    
    print(f'5 и \"test\": {str_compare(5, "test")}')
    print(f'5 и \"5\": {str_compare(5, "5")}')
    print(f'5+5 и 1000: {str_compare(5+5, 1000)}')
    print(f'100 и 100: {str_compare(100, 100)}')
    print(f'\"Privet\" и \"Privet\": {str_compare("Privet", "Privet")}')
    print(f'\"Mir\" и \"mir\": {str_compare("Mir", "mir")}')
    print(f'\"Privet, mir\" и \"Privet\": {str_compare("Privet, mir", "Privet")}')
    print(f'\"Privet\" и \"Privet, mir\": {str_compare("Privet", "Privet, mir")}')
    print(f'\"Privet, mir\" и \"learn\": {str_compare("Privet, mir", "learn")}')
    print(f'\"mir\" и \"learn\": {str_compare("mir", "learn")}')
    print(f'\"learn\" и \"learn\": {str_compare("learn", "learn")}')


if __name__ == "__main__":
    main()
