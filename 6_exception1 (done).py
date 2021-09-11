"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user(answ):
    while True:
          try:
            hello = input('Как дела?')
            if answ != 'Хорошо':
                  answ = hello
                  
          except KeyboardInterrupt:
            print('Пока')
            break
    

print(hello_user('Плохо'))
