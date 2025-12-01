from class_Calculator import Calculator


class CalculatorApp:
    """Класс приложения — управляет взаимодействием с пользователем."""
    
    def __init__(self):
        self.calc = Calculator()  # Экземпляр калькулятора
        self.history = []        # История вычислений

    def get_number(self, prompt):
        """Ввод числа с обработкой ошибок."""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Ошибка: введите число!")

    def show_menu(self):
        """Вывод меню операций."""
        print("\n=== Калькулятор (ООП) ===")
        print("1. Сложение (+)")
        print("2. Вычитание (-)")
        print("3. Умножение (*)")
        print("4. Деление (/)")
        print("5. Возведение в степень (x^y)")
        print("6. Квадратный корень (√x)")
        print("7. Процент (x% от y)")
        print("8. История вычислений")
        print("9. Выход")

    def log_operation(self, operation, result):
        """Запись операции в историю."""
        self.history.append(f"{operation} = {result}")

    def show_history(self):
        """Показ истории вычислений."""
        if not self.history:
            print("История пуста.")
        else:
            print("\nИстория вычислений:")
            for entry in self.history:
                print(entry)

    def run(self):
        """Основной цикл приложения."""
        while True:
            self.show_menu()
            choice = input("\nВыберите операцию (1–9): ").strip()

            if choice == '9':
                print("До свидания!")
                break

            if choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
                print("Ошибка: неверный выбор!")
                continue

            if choice == '8':  # Показать историю
                self.show_history()
                continue

            # Ввод чисел
            if choice == '6':  # Квадратный корень
                num1 = self.get_number("Введите число: ")
                try:
                    result = self.calc.sqrt(num1)
                    operation = f"√{num1}"
                except ValueError as e:
                    print(e)
                    continue

            elif choice == '7':  # Процент
                num1 = self.get_number("Введите процент: ")
                num2 = self.get_number("Введите число: ")
                result = self.calc.percentage(num1, num2)
                operation = f"{num1}% от {num2}"

            else:  # Остальные операции (требуют два числа)
                num1 = self.get_number("Введите первое число: ")
                num2 = self.get_number("Введите второе число: ")

                if choice == '1':
                    result = self.calc.add(num1, num2)
                    operation = f"{num1} + {num2}"
                elif choice == '2':
                    result = self.calc.subtract(num1, num2)
                    operation = f"{num1} - {num2}"
                elif choice == '3':
                    result = self.calc.multiply(num1, num2)
                    operation = f"{num1} * {num2}"
                elif choice == '4':
                    try:
                        result = self.calc.divide(num1, num2)
                        operation = f"{num1} / {num2}"
                    except ValueError as e:
                        print(e)
                        continue
                elif choice == '5':
                    result = self.calc.power(num1, num2)
                    operation = f"{num1} ^ {num2}"

            # Вывод результата и запись в историю
            print(f"Результат: {result}")
            self.log_operation(operation, result)






