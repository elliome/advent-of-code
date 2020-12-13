with open('passwords.txt') as f:
    passwords = f.read().splitlines()

# Test the password against the policy  
def TestPassword(min, max, char, password):
    # check if the number of occurances is between or equal to the minimum and the maximum 
    if  password.count(char) >= min and password.count(char) <= max:
        return 1
    else:
        return 0

# default success count to 0
success_count = 0

# Loop through the passwords
for password in passwords:
    min_count = None
    max_count = None
    match_char = None
    string = None

    temp = ""

    # for each character in the line
    for index, char in enumerate(password):
        if char == " " and max_count != None:
            continue
        elif char == "-":
            min_count = int(temp)
            temp = ""
            continue
        elif char == " ":
            max_count = int(temp)
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
    
    success_count += TestPassword(min_count, max_count, match_char, string)

print(success_count)