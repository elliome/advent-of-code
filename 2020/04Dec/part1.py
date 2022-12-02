class Passport:
    records = []

    @staticmethod
    def ValidCheck():
        valid_count = 0

        for passport in Passport.records:
            if passport.__ValidCheck():
                valid_count += 1
        
        return valid_count

    def __init__(self, string):
        Passport.records.append(self)
        self.input = string
        self.fields = {
            "byr": None,
            "iyr": None,
            "eyr": None,
            "hgt": None,
            "hcl": None,
            "ecl": None,
            "pid": None,
            "cid": None
        }

        temp_key = ""
        temp_value = ""
        reading = "key"
        for _index, char in enumerate(string):

            if char in [" ", "\n"]:
                self.__AddToField(temp_key, temp_value)
                temp_key = ""
                temp_value = ""
                reading = "key"
                continue
            elif char == ":":
                reading = "value"
                continue

            if reading == "key":
                temp_key += char
            elif reading == "value":
                temp_value += char
        self.__AddToField(temp_key, temp_value)


    def __AddToField(self, key, value):
        self.fields[key] = value

    def __ValidCheck(self):
        for key, value in self.fields.items():
            if value == None and key != "cid":
                return False

        return True

    def __str__(self):
        return f"{self.fields} --- [{self.__ValidCheck()}]"


with open('passports.txt') as f:
    inputs = f.read().split("\n\n")

for _input in inputs:
    Passport(_input)

print(Passport.ValidCheck())