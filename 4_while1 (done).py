"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user(answ):
      
      while True:
            if answ != 'Хорошо':
                  answ = input('Как дела?')
                  
            else:
                  break
hello = input('Как дела?')
print(hello_user(hello))
    

    

