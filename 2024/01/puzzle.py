with open('input.txt') as f:
    numbers = f.read().splitlines()

colA = []
colB = []

for line in numbers:
    first, second = line.split("   ")
    colA.append(int(first))
    colB.append(int(second))

# Part 1

colA.sort()
colB.sort()

totalDistance = 0

for index in range(len(colA)):
    a = colA[index]
    b = colB[index]

    if a > b:
        totalDistance += a - b
    else:
        totalDistance += b - a

print(totalDistance)

# Part 2

colADict = {}

for number in colA:
    colADict[number] = 0

for number in colB:
    if number in colADict:
        colADict[number] += 1

totalSimilarityScore = 0

for key, value in colADict.items():
    totalSimilarityScore += key * value
    
print(totalSimilarityScore)