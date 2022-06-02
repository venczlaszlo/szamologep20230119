# paraméterek bekérése
D = float(input("Kérem a d oldalt"))
B = float(input("Kérem a b oldalt"))
A = float(input('Kérem az a oldalt: '))
C = float(input('Kérem a c oldalt: '))
M = float(input('Kérem a magasságot: '))

# terület számítás
terület = 0.5 * (A + C) * M

# sulyvonal számítás
sulyvonal = 0.5 * (A + C)

# kerület számítás
kerület = A + B + C + D

# végeredmény nyomtatása
print("\n A trapéz területe = %.2f " %terület)
print("\n A trapéz súlyvonala = %.2f " %sulyvonal)
print("\n A trapéz kerülete = %.2f " %kerület)