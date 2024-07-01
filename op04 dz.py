import random, math

def sum_range(start, end):
  sum_range = 0 
  
  # Если start больше, чем end, то поменяем их местами, чтобы избежать ошибок
  if start > end:
      start, end = end, start


  for i in range(start, end+1):
    sum_range = sum_range + i
  
  return sum_range

def square(side_length):
  perimeter = 4 * side_length
  area = side_length ** 2
  diagonal = side_length * math.sqrt(2)
  return perimeter, area, diagonal

def bank(a, years):
  for _ in range(years):
      a += a * 0.10  # увеличиваем вклад на 10%
  return a


print('Сумма чисел')
start = int(random.random()*10)   
end = int(random.random()*10)   

result = sum_range(start, end)
if start > end:
  start, end = end, start
print(f"Сумма чисел от {start} до {end} = {result}")  

print('-'*20)

print('Периметр, площадь и диагональ квадрата')
side = int(random.random()*10) 
result = square(side)
print(f"Сторона квадрата: {side}, Периметр: {result[0]}, Площадь: {result[1]}, Диагональ: {result[2]:.2f}")

print('-'*20)

initial_amount = int(random.random()*1000)   # начальная сумма вклада
years = int(random.random()*10)   # количество лет
print(f'Вклад в размере {initial_amount} рублей сроком на {years} лет под 10% годовых')
final_amount = bank(initial_amount, years)
print(f"Сумма на счету через {years} лет: {final_amount:.2f} рублей")