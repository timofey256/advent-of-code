import re

file = open("input.txt", "r")
lines = file.read().split('\n')
lines = lines[:len(lines)-2]
MATCHES = [
    [(int(m[1]), m.span()) for m in re.finditer(r"(\d+)", line)] for line in lines 
]
H, W = len(lines), len(lines[0])
COORDS = {}

def find_symbol(y, x1, x2):
    for v in [y - 1, y, y + 1]:
        for u in range(x1 - 1, x2 + 1):
            if 0 <= v < H and 0 <= u < W and lines[v][u] not in ".0123456789":
                return v, u


def find_all_symbols():
    for y, line in enumerate(MATCHES):
        for part, (x1, x2) in line:
            if coord := find_symbol(y, x1, x2):
                COORDS.setdefault(coord, []).append(part)


find_all_symbols()


if __name__ == "__main__":
    print(sum(sum(parts) for parts in COORDS.values())) # part 1
    print(sum(a * b[0] for a, *b in COORDS.values() if b)) # part 2
