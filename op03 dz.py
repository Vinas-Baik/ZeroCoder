print('Поиск наименьшего числа')
# Создаем пустой список для хранения чисел
numbers = []

# Запрашиваем у пользователя ввод трех чисел в цикле
count = 0
while count < 3:
  numbers.append(int(input(f"Введите число {count + 1}: ")))
  count += 1

# Находим наименьшее число в списке и 
# выводим результат
print("Наименьшее число:", min(numbers))

print('-'*20)

print('Простой калькулятор')

print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

choice = input("Введите номер операции (1/2/3/4): ")

if choice in ['1', '2', '3', '4']:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
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
else:
    print("Ошибка: некорректный выбор операции!")

print('-'*20)

print('Определение количества дней в месяце')

# Создаем словарь, в котором ключами являются номера месяцев, а значениями - количество дней в этих месяцах
days_in_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# Запрашиваем у пользователя номер месяца
month = int(input("Введите номер месяца (1-12): "))

# Проверяем, является ли введенный номер месяца допустимым
if 1 <= month <= 12:
    # Выводим количество дней в введенном месяце
    print(f"Количество дней в месяце: {days_in_month[month]}")
else:
    # Сообщаем пользователю, что введенный номер месяца недопустим
    print("Неверный номер месяца. Пожалуйста, введите число от 1 до 12.")


print('-'*20)


print('Проверка на четность чисел в диапазоне')

# Запрашиваем у пользователя начало и конец диапазона
start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

chet_list = []
# Перебираем числа в диапазоне от start до end включительно
for number in range(start, end + 1):
    # Проверяем, является ли число четным
    if number % 2 == 0:
        chet_list.append(number)

print("Четные числа в диапазоне [",start,":",end,"]:", chet_list)

print('-'*20)

print('Игра: камень ножницы бумага')

# Инициализация счетчиков побед
score_player1 = 0
score_player2 = 0

# Словарь для определения победителя
win_map = {
    'камень': 'ножницы',
    'ножницы': 'бумага',
    'бумага': 'камень'
}

# Основной игровой цикл
while score_player1 < 3 and score_player2 < 3:
    # Получение ввода от игроков
    player1_choice = input("Игрок 1, введите ваш выбор (камень, ножницы, бумага): ").strip().lower()
    player2_choice = input("Игрок 2, введите ваш выбор (камень, ножницы, бумага): ").strip().lower()

    # Проверка валидности ввода
    if player1_choice not in win_map or player2_choice not in win_map:
        print("Неправильный выбор. Пожалуйста, введите 'камень', 'ножницы' или 'бумага'.")
        continue

    # Определение победителя раунда
    if player1_choice == player2_choice:
        print("Ничья!")
    elif win_map[player1_choice] == player2_choice:
        print("Игрок 1 выиграл раунд!")
        score_player1 += 1
    else:
        print("Игрок 2 выиграл раунд!")
        score_player2 += 1

    # Вывод текущего счета
    print(f"Счет: Игрок 1 - {score_player1}, Игрок 2 - {score_player2}")

# Определение и вывод окончательного победителя
if score_player1 == 3:
    print("Игрок 1 выиграл игру!")
else:
    print("Игрок 2 выиграл игру!")