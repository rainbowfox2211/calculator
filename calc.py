import math

def add(x, y):
    """Сложение"""
    return x + y

def subtract(x, y):
    """Вычитание"""
    return x - y

def multiply(x, y):
    """Умножение"""
    return x * y

def divide(x, y):
    """Деление с проверкой на ноль"""
    if y == 0:
        return "Ошибка: деление на ноль!"
    return x / y

def power(x, y):
    """Возведение в степень"""
    return x ** y

def sqrt(x):
    """Квадратный корень"""
    if x < 0:
        return "Ошибка: корень из отрицательного числа!"
    return math.sqrt(x)

def percentage(x, y):
    """Процент от числа (x% от y)"""
    return (x / 100) * y

def show_menu():
    """Вывод меню операций"""
    print("\n=== Калькулятор ===")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Возведение в степень (x^y)")
    print("6. Квадратный корень (√x)")
    print("7. Процент (x% от y)")
    print("8. Выход")

def get_number(prompt):
    """Ввод числа с обработкой ошибок"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число!")

def main():
    """Основная функция программы"""
    while True:
        show_menu()
        choice = input("\nВыберите операцию (1-8): ").strip()
        
        if choice == '8':
            print("До свидания!")
            break
            
        if choice not in ['1', '2', '3', '4', '5', '6', '7']:
            print("Ошибка: неверный выбор!")
            continue
        
        # Ввод чисел
        if choice == '6':  # Квадратный корень
            num1 = get_number("Введите число: ")
            result = sqrt(num1)
        elif choice == '7':  # Процент
            num1 = get_number("Введите процент: ")
            num2 = get_number("Введите число: ")
            result = percentage(num1, num2)
        else:  # Остальные операции
            num1 = get_number("Введите первое число: ")
            num2 = get_number("Введите второе число: ")
            
            # Выбор операции
            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
            elif choice == '5':
                result = power(num1, num2)
        
        print(f"Результат: {result}")

if __name__ == "__main__":
    main()