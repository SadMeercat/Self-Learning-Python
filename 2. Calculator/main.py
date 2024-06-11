# Задача: Калькулятор с историей операций
# Напишите программу, которая будет выполнять основные арифметические операции (сложение, вычитание, умножение, деление) и сохранять историю всех операций.

# Условия:
# Программа должна предоставлять пользователю меню с возможностями выбора операции: сложение, вычитание, умножение, деление и просмотр истории операций.
# После выбора операции, программа должна запрашивать два числа для выполнения операции.
# Программа должна выводить результат операции.
# Программа должна сохранять историю всех выполненных операций и предоставлять возможность просмотреть её.

def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a/b
    else:
        return "Деление на 0 невозможно"
    
if __name__ == '__main__':
    history = []

    while True:
        print('Выберете оперцию: ')
        print('1. Сложение')
        print('2. Вычитание')
        print('3. Умножение')
        print('4. Деление')
        print('5. История операций')
        print('6. Выход')

        choice = input('Ваш выбор: ')
        
        if choice in ['1','2','3','4']:
            a = float(input('Введите первое число: '))
            b = float(input('Введите второе число: '))
            if choice == 1:
                result = sum(a,b)
                history.append(f'{a} + {b} = {result}')
                print(f'{a} + {b} = {result}')
            elif choice == 2:
                result = sub(a,b)
                history.append(f'{a} - {b} = {result}')
                print(f'{a} - {b} = {result}')
            elif choice == 3:
                result = mul(a,b)
                history.append(f'{a} * {b} = {result}')
                print(f'{a} * {b} = {result}')
            elif choice == 4:
                result = div(a,b)
                history.append(f'{a} / {b} = {result}')
                print(f'{a} / {b} = {result}')
        elif choice == '5':
            if history:
                print('История операций: ')
                for i in range(len(history)):
                    print(f'{i + 1}. {history[i]}')
            else: 
                print('История операций пуста')
        elif choice == '6':
            break
        else:
            print('Некорректный ввод')
        print()