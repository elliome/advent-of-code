class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __str__(self): 
        return f"({self.x}, {self.y})"

def returnStripped(s):
    return s.strip()

with open('trees.txt') as f:
    trees = f.read().splitlines()

trees = list(map(returnStripped, trees))
tile_width = len(trees[0])


# part2
slopes = [
    Vector2(1,1),
    Vector2(3,1),
    Vector2(5,1),
    Vector2(7,1),
    Vector2(1,2)
]

trees_encountered = []

for slope in slopes:
    temp_trees_encountered = 0
    position = Vector2(slope.x,slope.y)

    while position.y < len(trees):
        row = trees[position.y]
        
        if row[position.x:position.x+1] == "#":
            temp_trees_encountered += 1
            print(row[:position.x] + '\033[92m' + row[position.x:position.x+1] + '\033[0m' + row[position.x + 1:])

        else:
            print(row[:position.x] + '\033[91m' + row[position.x:position.x+1] + '\033[0m' + row[position.x + 1:])

        position += slope
        if position.x >= tile_width:
            position.x -= tile_width
        
    print(temp_trees_encountered)
    trees_encountered.append(temp_trees_encountered)
    print(f"Tile width: {tile_width}")
    print(f"Tile length: {len(trees)}")
    input()

print(trees_encountered)

multiplied_together = 1

for x in trees_encountered:
    multiplied_together *= x

print(multiplied_together)