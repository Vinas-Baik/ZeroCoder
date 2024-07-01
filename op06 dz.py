import arithmetic 
import random

def select_students(students, num_to_select=5):
  """
  Функция случайным образом выбирает уникальные имена из списка учащихся.

  :param students: Список имён учащихся.
  :param num_to_select: Количество учащихся, которых нужно выбрать.
  :return: Список выбранных имён.
  """
  if len(students) < num_to_select:
      raise ValueError("Количество учащихся меньше, чем количество требуемых выборов.")

  return random.sample(students, num_to_select)


def write_file():
  # Запрашиваем у пользователя ввод текста
  user_input = input("Введите текст, который хотите записать в файл: ")

  # Открываем файл в режиме записи (создаст файл, если его нет)
  with open('user_data.txt', 'w', encoding='utf-8') as file:
      # Записываем введенный текст в файл
      file.write(user_input)

  print("Текст успешно записан в файл user_data.txt")


def arithmetic_operations():
  # Сложение
  result_add = arithmetic.add(5, 3)
  print(f"5 + 3 = {result_add}")

  # Вычитание
  result_subtract = arithmetic.subtract(5, 3)
  print(f"5 - 3 = {result_subtract}")

  # Умножение
  result_multiply = arithmetic.multiply(5, 3)
  print(f"5 * 3 = {result_multiply}")

  # Деление
  result_divide = arithmetic.divide(5, 3)
  print(f"5 / 3 = {result_divide}")

students_list = [
    "Алексей", "Мария", "Иван", "Елена", "Сергей",
    "Анна", "Дмитрий", "Ольга", "Кирилл", "Татьяна",
    "Николай", "Юлия", "Михаил", "Анастасия", "Максим"
]


print('Задание 1. Создание и запись в файл')

write_file()

print('-'*30 )
print('Задание 2. Создание модуля с функциями арифметики ')

arithmetic_operations()

print('-'*30 )
print('Задание 3. Случайный выбор элемента ')

selected_students = select_students(students_list, 5)

print("Выбранные учащиеся для ответа на уроке:")
for student in selected_students:
    print(student)