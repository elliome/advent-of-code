from time import sleep

def rangeCheck(val, _min, _max):
    if val == None:
       raise Exception()

    if int(val) < _min or int(val) > _max:
        raise Exception()


class Passport:
    records = []

    @staticmethod
    def ValidCheck():
        valid_count = 0
        for passport in Passport.records:
            if passport.__ValidCheck():
                valid_count += 1
        
        return valid_count

    @staticmethod
    def BYRCheck(byr):
        rangeCheck(byr, 1920, 2002)

    @staticmethod
    def IYRCheck(iyr):
        rangeCheck(iyr, 2010, 2020)

    @staticmethod
    def EYRCheck(eyr):
        rangeCheck(eyr, 2020, 2030)

    @staticmethod
    def HGTCheck(hgt):
        if hgt[-2:] == "cm":
            rangeCheck(hgt[:-2], 150, 193)
        elif hgt[-2:] == "in": 
            rangeCheck(hgt[:-2], 59, 76)
        else:
            raise Exception()

    @staticmethod
    def HCLCheck(hcl):
        if hcl[:1] != "#":
            raise Exception()
        
        if len(hcl) > 7:
            raise Exception()
        else:
            int(f"{hcl[1:]}", 16)

    @staticmethod
    def ECLCheck(ecl):
        if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            raise Exception()
        
    @staticmethod
    def PIDCheck(pid):
        if len(pid) != 9:
            raise Exception()
        
        int(pid)

    def __init__(self, string):
        Passport.records.append(self)
        self.input = string
        self.fields = {
            "byr": None, # 1920 >= and <= 2002
            "iyr": None, # 2010 >= and <= 2020
            "eyr": None, # 2020 >= and <= 2030
            "hgt": None, # 
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
        try:
            Passport.BYRCheck(self.fields['byr'])
            Passport.IYRCheck(self.fields['iyr'])
            Passport.EYRCheck(self.fields['eyr'])
            Passport.HGTCheck(self.fields['hgt'])
            Passport.HCLCheck(self.fields['hcl'])
            Passport.ECLCheck(self.fields['ecl'])
            Passport.PIDCheck(self.fields['pid'])
        except:
            return False
        else:
            return True
        

    def __str__(self):
        return f"{self.fields} --- [{self.__ValidCheck()}]"


with open('passports.txt') as f:
    inputs = f.read().split("\n\n")

for _input in inputs:
    Passport(_input)

print(Passport.ValidCheck())