def solve():
    file = open("input.txt", "r")
    
    total = 0
    for line in file:
        if line == '\n':
            break
        left = set(line.split(': ')[1].split('|')[0].split())
        right = set(line.split(': ')[1].split('|')[1].split())
        intersection_power = len(left.intersection(right))
        # print(f"left: {left},\n rigth : {right},\n intersection: {intersection_power}\n")
        
        if intersection_power > 0:
            total += pow(2, intersection_power-1)
    print(total)
    
        
if __name__ == "__main__":
    solve()
