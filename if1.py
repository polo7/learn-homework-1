"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    def get_occupation(age):
      if age >= 3 and age <= 7:
        occupation = 'должны ходить в детский сад'
      elif age > 7 and age <= 18:
        occupation = 'должны учиться в школе'
      elif age > 18 and age <= 23:
        occupation = 'должны учиться в ВУЗе'
      elif age > 23 and age <= 65:
        occupation = 'должны работать'
      else:
        occupation = 'ничем не занимаетесь'
      return occupation

    user_age = int(input('Введите ваш возраст (целое число больше ноля): '))
    occupation = get_occupation(user_age)
    print(f'Судя по возрасту, вы {occupation}.')


    

if __name__ == "__main__":
    main()
