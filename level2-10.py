n = int(input("enter the num:"))
piles = []
stones = 1 if n % 2 == 0 else 2  
for i in range(n // 2):
    piles.append(stones)
    stones += 2
print("Stones in a single pile =", piles)
