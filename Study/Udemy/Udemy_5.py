while True:
    first_input, second_input = float(input("Enter first number")), float(input("Enter second number"))
    try:
        if second_input == 0:
            raise ValueError("Enter not 0")
        print(first_input / second_input)

    except ValueError:
        print("Try to enter some more")
        continue

    answer = input("Do you want to quit?")

    if answer == 'yes':
        break
    else:
        continue
