def is_valid(num):
    return num.isdigit() and 0 <= int(num) <= 100

def is_end(s):
    return s in ('нет','стоп')

def input_num():
     while True:
        print('Введите число: ', end = ' ')
        guess = input()
        if is_valid(guess):
            return int(guess)
        elif is_end(guess):
            return(guess)
        elif guess == 'хуй':
            print('Сам ты хуй, быдло\n')
        elif guess == 'макан':
            print('хуесос\n')
        elif guess == 'Россия':
            print('Для русских\n')
        else:
             print('Вы ввели неверное значение.', end = ' ')  

def is_even():
    while True:
        n = input_num()
        if n in ('нет','стоп'):
            print('''
        ****************
        До новых встреч!
        ****************
''')
            break
        elif n % 2 == 0:
            print('Число', n, 'четное\n')     
        else:
            print('Число', n, 'нечетное\n')

print('''                                 
        *************************************
        Добро пожаловать в определитель чисел
        *************************************
        
Напишите число от 1 до 100 и узнайте четное оно или нет''')

is_even()