def solve():
    file = open("input.txt", "r")
    lines = file.read().split('\n')
    lines = lines[:len(lines)-2]
    
    total = 0
    multipliers = [1]*len(lines)
    
    for i, line in enumerate(lines):
        print(line)
        left = set(line.split(': ')[1].split('|')[0].split())
        right = set(line.split(': ')[1].split('|')[1].split())
        intersection_power = len(left.intersection(right))
        # print(f"left: {left},\n rigth : {right},\n intersection: {intersection_power}\n")
        
        if intersection_power > 0:
            total += multipliers[i]*pow(2, intersection_power-1)
        #print(f"total after i={i} : {total}")
        for j in range(1, intersection_power+1):
            multipliers[i+j] += multipliers[i]

    print(sum(multipliers))
        
if __name__ == "__main__":
    solve()
