import clips


def calcValue(x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i == 0 and j == 0):
                pass
            new_x = x + i
            new_y = y + j
            if ((new_x, new_y) in bomb_loc):
                count += 1
    return count


bomb_loc = []

b_size = int(input("Masukkan ukuran board: "))
bomb_count = int(input("Masukkan jumlah bomb: "))


env = clips.Environment()

# Assert the first ordeded-fact as string so its template can be retrieved
bomb_template = """
(deftemplate bomb
 (slot x_loc (type INTEGER) (default ?DERIVE))
 (slot y_loc (type INTEGER) (default ?DERIVE))
)
"""
env.build(bomb_template)

tile_template = """
(deftemplate tile
 (slot x_loc (type INTEGER) (default ?DERIVE))
 (slot y_loc (type INTEGER) (default ?DERIVE))
 (slot value (type INTEGER) (default ?DERIVE))
)
"""
env.build(tile_template)

bomb = env.find_template('bomb')
for i in range(bomb_count):
    x_loc = int(input())
    y_loc = int(input())
    bomb_loc.append((x_loc, y_loc))
    new_fact = bomb.new_fact()
    new_fact['x_loc'] = clips.Symbol(str(x_loc))
    new_fact['y_loc'] = clips.Symbol(str(y_loc))
    new_fact.assertit()

tile = env.find_template('tile')
for i in range(b_size):
    for j in range(b_size):
        if (not ((i, j) in bomb_loc)):
            new_fact = tile.new_fact()
            new_fact['x_loc'] = clips.Symbol(str(i))
            new_fact['y_loc'] = clips.Symbol(str(j))
            new_fact['value'] = clips.Symbol(str(calcValue(i, j)))
            new_fact.assertit()

print(bomb_loc)

for fact in env.facts():
    print(fact)

# env.run()
