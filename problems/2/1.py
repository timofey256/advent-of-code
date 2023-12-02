if __name__ == "__main__":
    red_max = 12
    green_max = 13
    blue_max = 14
    
    file = open("input.txt", "r")
    total = 0
    for line in file:
        if line.strip() == "":
            break

        words = line.split()
        current_id = None
        can_fit = True
        
        for i, word in enumerate(words):
            if word == "Game":
                current_id = int(words[i+1][:-1])
            
            if word.isdigit():
                number = int(word)
                if words[i+1].startswith("blue") and number > blue_max:
                    can_fit = False
                if words[i+1].startswith("red") and number > red_max:
                    can_fit = False
                if words[i+1].startswith("green") and number > green_max:
                    can_fit = False
        
        if can_fit:
            print(f"adding id={id}")
            total += current_id

    print(total)
