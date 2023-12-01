def solve():
    file = open("input.txt", "r")
    result = 0
    for line in file:
        first = None
        last = None
        for i, char in enumerate(line):
            if char.isdigit():
                if first is None:
                    first = char
                last = char

        if first is not None:
            result += int(first+last)
    print(result)

if __name__ == "__main__":
    solve()
