import datetime
import math
import random
import uuid
import time
import file_module


def datetime_menu():
    while True:
        print("\nDatetime and Time Operations")
        print("1. Display current date and time")
        print("2. Difference between two dates")
        print("3. Format date")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back")

        ch = input("Enter choice: ")

        if ch == "1":
            now = datetime.datetime.now()
            print("Current Date and Time:", now)

        elif ch == "2":
            d1 = input("Enter first date (YYYY-MM-DD): ")
            d2 = input("Enter second date (YYYY-MM-DD): ")

            date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
            date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")

            print("Difference:", abs((date2 - date1).days), "days")

        elif ch == "3":
            now = datetime.datetime.now()
            print(now.strftime("%d-%m-%Y %I:%M %p"))

        elif ch == "4":
            input("Press ENTER to start stopwatch")
            start = time.time()
            input("Press ENTER to stop")
            end = time.time()
            print("Elapsed Time:", round(end - start, 2), "seconds")

        elif ch == "5":
            sec = int(input("Enter seconds: "))
            for i in range(sec, 0, -1):
                print(i)
                time.sleep(1)
            print("Time's up!")

        elif ch == "6":
            break

def math_menu():
    while True:
        print("\nMathematical Operations")
        print("1. Factorial")
        print("2. Compound Interest")
        print("3. Trigonometry")
        print("4. Area of Circle")
        print("5. Back")

        ch = input("Enter choice: ")

        if ch == "1":
            n = int(input("Enter number: "))
            print("Factorial:", math.factorial(n))

        elif ch == "2":
            p = float(input("Principal: "))
            r = float(input("Rate (%): "))
            t = float(input("Time (years): "))
            amount = p * (1 + r/100) ** t
            print("Compound Interest:", round(amount, 2))

        elif ch == "3":
            angle = float(input("Enter angle in degrees: "))
            rad = math.radians(angle)
            print("Sin:", math.sin(rad))

        elif ch == "4":
            r = float(input("Enter radius: "))
            print("Area:", math.pi * r * r)

        elif ch == "5":
            break


def random_menu():
    while True:
        print("\nRandom Data Generation")
        print("1. Random Number")
        print("2. Random List")
        print("3. Random Password")
        print("4. Random OTP")
        print("5. Back")

        ch = input("Enter choice: ")

        if ch == "1":
            print(random.randint(1, 100))

        elif ch == "2":
            print([random.randint(1, 50) for _ in range(5)])

        elif ch == "3":
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#"
            length = int(input("Password length: "))
            password = "".join(random.choice(chars) for _ in range(length))
            print("Generated Password:", password)

        elif ch == "4":
            otp = random.randint(1000, 9999)
            print("OTP:", otp)

        elif ch == "5":
            break


def generate_uuid():
    print("Generated UUID:", uuid.uuid4())


def file_menu():
    while True:
        print("\nFile Operations")
        print("1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Append File")
        print("5. Back")

        ch = input("Enter choice: ")

        if ch == "1":
            name = input("Enter file name: ")
            file_module.create_file(name)

        elif ch == "2":
            name = input("File name: ")
            data = input("Enter data: ")
            file_module.write_file(name, data)

        elif ch == "3":
            name = input("File name: ")
            file_module.read_file(name)

        elif ch == "4":
            name = input("File name: ")
            data = input("Enter data: ")
            file_module.append_file(name, data)

        elif ch == "5":
            break

def explore_module():
    mod = input("Enter module name: ")
    module = __import__(mod)
    print("Available Attributes:")
    print(dir(module))


def main():
    while True:
        print("\n===== Multi-Utility Toolkit =====")
        print("1. Datetime Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate UUID")
        print("5. File Operations")
        print("6. Explore Module (dir())")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            datetime_menu()
        elif choice == "2":
            math_menu()
        elif choice == "3":
            random_menu()
        elif choice == "4":
            generate_uuid()
        elif choice == "5":
            file_menu()
        elif choice == "6":
            explore_module()
        elif choice == "7":
            print("Program Ended")
            break

if __name__ == "__main__":
    main()