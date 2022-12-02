with open('numbers.txt') as f:
    numbers = f.read().splitlines()

for index, number in enumerate(numbers):
    numbers[index] = int(number)

for index, number1 in enumerate(numbers):
    for number2 in numbers[index:]:        
        if number1 + number2 == 2020:
            print(f"{number1} + {number2} = {number1 + number2}. {number1} * {number2} = {number1*number2}")