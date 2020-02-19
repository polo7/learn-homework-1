"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    school_grades = [
      {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
      {'school_class': '5a', 'scores': [2, 2, 2, 2, 2]},
      {'school_class': '7a', 'scores': [5, 5, 5, 5, 5]},
    ]

    # Если порядок вывода не важен, то можно так:
    # сразу выводим среднюю оценку по классам и в конце по школе.
    print('Вариант 1')
    print('Сначала средние оценки по классам и потом по школе')

    school_medium_sum = 0

    for klass in school_grades:
      class_medium = round(sum(klass["scores"]) / len(klass["scores"]), 2)
      print(f'Средняя оценка в классе {klass["school_class"]}: {class_medium}')
      school_medium_sum += class_medium
    
    # Если переменную используем 1 раз только для печати, то надо ли ее заводить, ради читаемости кода?
    #school_medium = school_medium_sum / len(school_grades)
    
    print(f'Средняя оценка по школе: {round(school_medium_sum / len(school_grades), 2)}')

    # Если важен порядок вывода как в условиях, то сначала надо посчитать общешколный средний,
    # а потом выводить средние оценки по классам.
    print('\nВариант 2')
    print('Как в условиях (сначала школа, потом классы)')
    
    school_medium_sum = 0
    
    for klass in school_grades:
      class_medium = round(sum(klass["scores"]) / len(klass["scores"]), 2)
      klass['medium_score'] = class_medium
      school_medium_sum += class_medium
    
    print(f'Средняя оценка по школе: {round(school_medium_sum / len(school_grades), 2)}')
    
    for klass in school_grades:
      print(f'Средняя оценка в классе {klass["school_class"]}: {klass["medium_score"]}')


if __name__ == "__main__":
    main()
