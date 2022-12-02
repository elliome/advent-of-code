with open('numbers.txt') as f:
    numbers = f.read().splitlines()

for index, number in enumerate(numbers):
    numbers[index] = int(number)

for index1, number1 in enumerate(numbers):
    for index2, number2 in enumerate(numbers[index1:]):  
        for index3, number3 in enumerate(numbers[index2:]):      
            if number1 + number2 + number3 == 2020:
                print(f"{number1} + {number2} + {number3} = {number1 + number2 + number3}. {number1} * {number2} * {number3} = {number1*number2*number3}")