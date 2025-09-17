
while True:
        num1 = input('Enter your first number or "exit": ')
        if num1 == "exit":
            break
        num1 = float(num1)
        operater = input('Enter your operater (+ - * /): ')
        num2 = float(input('Enter your second number: '))
        show_history = input('Do you want to see history? (yes/no): ')
        history = show_history.lower()


        result = None

        if operater == '+':
                result = num1 + num2
                print(f'Result: {num1} {operater} {num2} = {result}')

        elif operater == '-':
                result = num1 - num2
                print(f'Result: {num1} {operater} {num2} = {result}')

        elif operater == '*':
                result = num1 * num2
                print(f'Result: {num1} {operater} {num2} = {result}')

        elif operater == '/':
                if num2 != 0:
                        result = num1 / num2
                        print(f'Result: {num1} {operater} {num2} = {result}')
                else:
                        print('Error: Division by zero')

        else:
                print('Invalid operator')

# Agar result calculate hua hai to file mein likho
        if result is not None:
                with open('history.txt', 'a') as file:
                        file.write(f'{num1} {operater} {num2} = {result}\n')

# History read karna
        if (history.lower() == 'yes') or history == 'Yes':
                with open('history.txt', 'r') as file:
                        print('----- History -----')
                        print(file.read())
                clear_history = input('Do you want to clear history? (yes/no): ')
                if clear_history.lower() == 'yes':
                        with open('history.txt', 'w') as file:
                                file.truncate()
                                print('History cleared.')
        

