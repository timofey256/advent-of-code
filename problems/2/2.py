if __name__ == "__main__":
    file = open("input.txt", "r")
    total = 0
    for line in file:
        if line.strip() == "":
            break

        red_min = 0
        green_min = 0
        blue_min = 0

        words = line.split()
        
        for i, word in enumerate(words):
            if word.isdigit():
                number = int(word)
                if words[i+1].startswith("blue"):
                    blue_min = max(blue_min, number)
                if words[i+1].startswith("red"):
                    red_min = max(red_min, number)
                if words[i+1].startswith("green"):
                    green_min = max(green_min, number)
        
        total += blue_min*red_min*green_min
    print(total)
