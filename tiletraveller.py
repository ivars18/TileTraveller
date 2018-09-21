
x = 1
y = 1
max_num = 3
while (True):
    if x == 1 and y == 1:
        print("You can travel: (N)orth.")
    elif x == 1 and y == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif x == 1 and y == 3:
        print("You can travel: (E)ast or (S)outh.")
    elif x == 2 and y == 1:
        print("You can travel: (N)orth.")
    elif x == 2 and y == 2:
        print("You can travel: (S)outh or (W)est.")
    elif x == 2 and y == 3:
        print("You can travel: (E)ast or (W)est.")
    elif x == 3 and y == 1:
        print("Victory!")
        break
    elif x == 3 and y == 2:
        print("You can travel: (N)orth or (S)outh.")
    elif x == 3 and y == 3:
        print("You can travel: (S)outh or (W)est.")
    while x <= max_num and y <= max_num:
        direction = input("Direction: ")
        if direction == "n" or direction == "N":
            if y == max_num or (x==2 and y ==2):
                print("Not a valid direction!")
            else:
                y += 1
                break
        elif direction == "s" or direction == "S":
            if (x == 2 and y == 3) or (x == 2 and y == 1) or (x == 3 and y == 1) or (x == 1 and y == 1):
                print("Not a valid direction!")
            else:
                y -= 1
                break
        elif direction == "w" or direction == "W":
            if x == 1 or (x == 3 and y == 2) or (x == 3 and y == 1) or (x == 2 and y == 1):
                print("Not a valid direction!")
            else:
                x -= 1
                break
        elif direction == "e" or direction == "E":
            if x == 3 or (x == 2 and y == 2) or (x == 2 and y == 1) or (x == 1 and y == 1):
                print("Not a valid direction!")
            else:
                x += 1
                break
        