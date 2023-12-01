def solve():
    spelled = [["one", "1"], ["two", "2"], ["three", "3"], ["four", "4"], ["five", "5"], ["six", "6"], ["seven", "7"], ["eight", "8"], ["nine", "9"]]
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
            for digit in spelled:
                if line.startswith(digit[0], i):
                    if first is None:
                        first = digit[1] 
                    last = digit[1]

        if first is not None:
            result += int(first+last)
    print(result)

if __name__ == "__main__":
    solve()
