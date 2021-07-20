def concat(strings: list[str]):
    out = ""
    for s in strings:
        out += s + " "
    return out[:-1]

file = open("moves")
out = open("moves_f", "wt")

moves = []
line = file.readline()
while line:
    moves.append(concat(line.split(" ")[1:-7]).replace("*", "").replace("\t", ""))
    line = file.readline()


out.write("[")
for move in moves:
    out.write('"' + move + '",')
out.write("]")