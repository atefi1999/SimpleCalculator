class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "❌ Error: Division by zero!"
        return a / b


class History:
    def __init__(self):
        self.operations = []

    def add_record(self, operation, result):
        self.operations.append(f"{operation} = {result}")

    def show_history(self):
        if not self.operations:
            print("📂 No history yet.")
        else:
            print("\n📜 Calculation History:")
            for idx, record in enumerate(self.operations, 1):
                print(f"{idx}. {record}")

    def clear_history(self):
        self.operations.clear()
        print("🧹 History cleared.")


class CalculatorCLI:
    def __init__(self):
        self.calculator = Calculator()
        self.history = History()

    def show_menu(self):
        print("\n🔢 Simple Calculator CLI")
        print("1️⃣ Add")
        print("2️⃣ Subtract")
        print("3️⃣ Multiply")
        print("4️⃣ Divide")
        print("5️⃣ Show History")
        print("6️⃣ Clear History")
        print("7️⃣ Exit")

    def get_user_input(self):
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b

    def run(self):
        while True:
            self.show_menu()
            choice = input("👉 Choose an option: ")

            if choice == "1":
                a, b = self.get_user_input()
                result = self.calculator.add(a, b)
                print(f"✅ Result: {result}")
                self.history.add_record(f"{a} + {b}", result)

            elif choice == "2":
                a, b = self.get_user_input()
                result = self.calculator.subtract(a, b)
                print(f"✅ Result: {result}")
                self.history.add_record(f"{a} - {b}", result)

            elif choice == "3":
                a, b = self.get_user_input()
                result = self.calculator.multiply(a, b)
                print(f"✅ Result: {result}")
                self.history.add_record(f"{a} * {b}", result)

            elif choice == "4":
                a, b = self.get_user_input()
                result = self.calculator.divide(a, b)
                print(f"✅ Result: {result}")
                self.history.add_record(f"{a} / {b}", result)

            elif choice == "5":
                self.history.show_history()

            elif choice == "6":
                self.history.clear_history()

            elif choice == "7":
                print("👋 Goodbye!")
                break

            else:
                print("❌ Invalid choice!")


if __name__ == "__main__":
    CalculatorCLI().run()
