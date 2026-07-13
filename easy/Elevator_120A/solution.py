with open("input.txt", "r") as fin:
    door = fin.readline().strip()
    rail = int(fin.readline())

with open("output.txt", "w") as fout:
    if (door == "front" and rail == 1) or (door == "back" and rail == 2):
        fout.write("L")
    else:
        fout.write("R")