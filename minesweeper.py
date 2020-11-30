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

env = clips.Environment()
env.load('minesweeper.clp')

# Minta input dari user
b_size = int(input("Masukkan ukuran board: "))
new_fact = "(b_size " + str(b_size) + ")"
fact = env.assert_string(new_fact)
bomb_count = int(input("Masukkan jumlah bomb: "))
new_fact = "(bomb_count " + str(bomb_count) + ")"
fact = env.assert_string(new_fact)

# Assert bomb fact
for i in range(bomb_count):
    x_loc = int(input())
    y_loc = int(input())
    bomb_loc.append((x_loc, y_loc))
    new_fact = "(bomb " + str(x_loc) + " " + str(y_loc) + ")"
    fact = env.assert_string(new_fact)

# Assert tile fact
for i in range(b_size):
    for j in range(b_size):
        if (not ((i, j) in bomb_loc)):
            new_fact = "(tile " + str(i) + " " + str(j) + \
                " " + str(calcValue(i, j)) + ")"
            fact = env.assert_string(new_fact)

# Assert unknown fact
for i in range(b_size):
    for j in range(b_size):
        if (not ((i, j) in bomb_loc)):
            new_fact = "(unknown " + str(i) + " " + str(j) + \
                " " + str(calcValue(i, j)) + ")"
            fact = env.assert_string(new_fact)
        else:
            new_fact = "(unknown " + str(i) + " " + str(j) + \
                " 9)"
            fact = env.assert_string(new_fact)

init_fact = "(user 0 0 0)"
fact = env.assert_string(init_fact)

# Print initial matrix
print("==== INITIAL BOARD ====")
for i in range(b_size):
    for j in range(b_size):
        print("X ", end="")
    print()

# env.run()
n = 1
while (len(list(env.activations())) != 0):
    env.run(limit=1)
    flags = []
    users = []
    # Retrieve flag
    for fact in env.facts():
        if (fact.template.name == 'flag'):
            flags.append((fact[0], fact[1]))
        elif (fact.template.name == 'user'):
            users.append((fact[0], fact[1], fact[2]))

      # Print board
    print("====== RUN KE " + str(n) + " ======")
    for i in range(b_size):
        for j in range(b_size):
            if ((j, i) in flags):
                print("- ", end="")
            elif ((j, i, calcValue(j, i)) in users):
                print(str(calcValue(j, i)) + " ", end="")
            else:
                print("X ", end="")
        print()
    n += 1

# Print flag
print("===== FINAL BOARD ====")
for i in range(4):
    for j in range(4):
        if ((j, i) in flags):
            print("- ", end="")
        else:
            print(str(calcValue(j, i)) + " ", end="")
    print()
