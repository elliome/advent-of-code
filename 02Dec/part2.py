with open('passwords.txt') as f:
    passwords = f.read().splitlines()


def TestPassword(min, max, char, password):

    if  password[min-1:min] == char and password[max-1:max] != char or password[min-1:min] != char and password[max-1:max] == char :
        return 1
    else:
        return 0

success_count = 0

for password in passwords:
    first_position = None
    second_position = None
    match_char = None
    string = None

    temp = ""

    for index, char in enumerate(password):
        if char == " " and second_position != None:
            continue
        elif char == "-":
            first_position = int(temp)
            temp = ""
            continue
        elif char == " ":
            second_position = int(temp)
            temp = ""
            continue
        elif char == ":":
            match_char = temp
            temp = ""
            continue
        elif index == len(password) - 1:
            string = temp + char
            continue

        temp += char
        
    success_count += TestPassword(first_position, second_position, match_char, string)

print(success_count)