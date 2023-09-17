from shapes import Circle, Triangle

def main():
    while True:
        print("\nВыберите фигуру:")
        print("1. Круг")
        print("2. Треугольник")
        print("3. Выйти")

        choice = input("Ваш выбор: ")

        if choice == "1":
            radius = float(input("Введите радиус круга: "))
            circle = Circle(radius)
            print(f"Площадь круга: {circle.area():.2f}")

        elif choice == "2":
            a = float(input("Введите сторону a: "))
            b = float(input("Введите сторону b: "))
            c = float(input("Введите сторону c: "))

            triangle = Triangle(a, b, c)
            print(f"Площадь треугольника: {triangle.area():.2f}")
            if triangle.is_right_triangle():
                print("Этот треугольник является прямоугольным.")
            else:
                print("Этот треугольник не является прямоугольным.")

        elif choice == "3":
            print("Выход...")
            break

        else:
            print("Неизвестный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
