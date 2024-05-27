# Завдання 1
# Користувач вводить із клавіатури три цифри. Необхідно створити число, що містить ці цифри. 
# Наприклад, якщо з клавіатури введено 1, 5, 7, тоді потрібно сформувати число 157.

first_digit = input("Введіть першу цифру: ")
second_digit = input("Введіть другу цифру: ")
trid_digit = input("Введыть третю цифру: ")
print(f"Результат: {first_digit}{second_digit}{trid_digit}")



# Завдання 2
# Користувач вводить із клавіатури число, що складається з чотирьох цифр. Потрібно знайти добуток цифр. 
# Наприклад, якщо з клавіатури введено 1324, тоді результат добутку 1*3*2*4 = 24.

digit = input("Введіть чотирьох значне число: ")
first_digit_symbol = int(digit[0])
second_digit_symbol = int(digit[1])
trid_digit_symbol = int(digit[2])
last_digit_symbol = int(digit[3])
result = first_digit_symbol * second_digit_symbol * trid_digit_symbol * last_digit_symbol
print(f"Результат: {result}")



# Завдання 3
# Користувач вводить з клавіатури кількість метрів. 
# Потрібно вивести результат переведення метрів у сантиметри, дециметри, міліметри, милі.

count_in_meters = int(input("Введіть кількість у метрах: "))
to_centimeter = count_in_meters * 100
to_decimeter = count_in_meters * 10
to_milimeter = count_in_meters * 1000
to_miles = count_in_meters * 0.000621371192
print(f"{count_in_meters}м = {to_centimeter}см")
print(f"{count_in_meters}м = {to_decimeter}дм")
print(f"{count_in_meters}м = {to_milimeter}мм")
print(f"{count_in_meters}м = {to_miles}миль")



# Завдання 4
# Напишіть програму, що обчислює площу трикутника. Користувач із клавіатури вводить розмір основи трикутника і розмір висоти.

triangle_base = int(input("Введіть розмір основи трикутника: "))
triangle_height = int(input("Введіть розмір висоти трикутника: "))
triangle_square = (triangle_base * triangle_height) / 2
print(f"Площа дорівнює: {triangle_square}")



# Завдання 5
# Користувач із клавіатури вводить чотиризначне число. Необхідно перевернути число і відобразити результат. 
# Наприклад, якщо введено 4512, результат — 2154.

digit = input("Введіть чотирьох значне число: ")
reversed_digit = str(digit)[::-1]
print(f"Результат: {reversed_digit}")



# Завдання 6
# Користувач вводить із клавіатури три числа. 
# Залежно від вибору користувача програма виводить на екран суму трьох чисел або добуток трьох чисел.

first_digit = int(input("Введіть перше число: "))
second_digit = int(input("Введіть друге число: "))
last_digit = int(input("Введіть третє число: "))
print("sum - вивести сумму цих чисел")
print("mul - вивести добуток цих чисел")
key = input("Введіть команду: ")
if key == "sum":
    print("Результат:")
    print(first_digit + second_digit + last_digit)

elif key == "mul":
    print("Результат:")
    print(first_digit * second_digit * last_digit)



# Завдання 7
# Користувач вводить із клавіатури три числа. 
# Залежно від вибору користувача програма виводить на екран максимум із трьох, мінімум із трьох 
# або середньоарифметичне трьох чисел.

first_digit = int(input("Введіть перше число: "))
second_digit = int(input("Введіть друге число: "))
last_digit = int(input("Введіть третє число: "))
arr = []
arr.insert(0, first_digit)
arr.insert(1, second_digit)
arr.insert(2, last_digit)
print("max - вивести максимум із цих чисел")
print("min - вивести мінімім із цих чисел")
print("ave - вивести середньоарифметичне із цих чисел")
key = input("Введіть команду: ")
if key == "max":
    print("Результат:")
    print(max(arr))

elif key == "min":
    print("Результат:")
    print(min(arr))

elif key == "ave":
    print("Результат:")
    print(sum(arr) / len(arr))



# Завдання 8
# Користувач вводить із клавіатури кількість метрів. 
# Залежно від вибору користувача програма конвертує метри в милі, дюйми або ярди.

count_in_meters = int(input("Введіть кількість у метрах: "))
print("miles - конвертувати в милі")
print("inches - конвертувати в дюйми")
print("yards - конвертувати в ярди")
key = input("Введіть команду: ")
if key == "miles":
    print("Результат:")
    print(count_in_meters * 0.000621371192)

elif key == "inches":
    print("Результат:")
    print(count_in_meters * 39.3700787)

elif key == "yards":
    print("Результат:")
    print(count_in_meters * 1.0936133) 