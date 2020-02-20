"""
Домашнее задание №1
Исключения: KeyboardInterrupt
* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

from datetime import datetime

def ask_user():
    """
    Замените pass на ваш код
    """
    qa_dict = {
      'Как дела?': 'Хорошо',
      'Что делаешь?': 'Учу Питон',
      'Как тебя зовут?': 'Рома',
      'Сколько тебе лет?': 'Неприлично спрашивать про возраст',
      'Который час?': datetime.now().time()
    }
    print('Привет. Задавай вопрос. Для списка вопросов спроси "О чем?"')
    while True:
      try:
        user_q = input('- ')
        if user_q in qa_dict:
          print(f'- {qa_dict[user_q]}')
        elif user_q == 'О чем?':
          print('===')
          for t in qa_dict:
            print(f'* {t}')
          print('===')
        else:
          print('- Давай закончим разговор.')
          break
      except KeyboardInterrupt:
        print('Пока!')
        break
    
if __name__ == "__main__":
    ask_user()