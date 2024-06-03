N1 = int(input("Enter a number:"))
S1 = input("enter the string:")
occupied_computers = set()
walked_away_count = 0
for letter in S1:
        if letter not in occupied_computers:
            if len(occupied_computers) < N1:
                occupied_computers.add(letter)
            else:
                walked_away_count += 1
        else:
            occupied_computers.remove(letter)

print(walked_away_count)
