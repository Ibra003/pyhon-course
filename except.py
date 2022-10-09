
try:
    # value = 10/0
    number = int(input("enter a number: "))

    print(number)
except ZeroDivisionError:

    print("Divided by zero")
except ValueError:
    print("invalid nput")


