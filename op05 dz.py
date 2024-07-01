def safe_divide(a, b):
  try:
      result = a / b
      return result
  except ZeroDivisionError:
      return None


def get_integer_from_user():
  while True:
      user_input = input("Пожалуйста, введите целое число: ")
      try:
          user_number = int(user_input)
          print(f"Вы ввели целое число: {user_number}")
          break
      except ValueError:
          print("Невозможно преобразовать введенное значение в целое число. Попробуйте еще раз.")

def calculate():
    print('Простой калькулятор')

    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")

    try:
        choice = input("Введите номер операции (1/2/3/4): ")
        if choice not in ['1', '2', '3', '4']:
            raise ValueError("Некорректный выбор операции")

        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: введено не число!")
        else:
            if choice == '1':
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
            elif choice == '2':
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")
            elif choice == '3':
                result = num1 * num2
                print(f"{num1} * {num2} = {result}")
            elif choice == '4':
                if num2 != 0:
                    result = num1 / num2
                    print(f"{num1} / {num2} = {result}")
                else:
                    print("Ошибка: деление на ноль!")
    except ValueError as e:
        print(e)
    

print('Задание 1: Базовая обработка исключений')
print(safe_divide(14, 26))    
print(safe_divide(26, 0))    
print(safe_divide(18, 6))    
print(safe_divide(20, 24))    
print(safe_divide(24, 0))    

print('-'*20)

print('Задание 2: Обработка множества видов исключений')

get_integer_from_user()

print('-'*20)

print('Задание 3: Обработка исключений прошлых программ')

calculate()