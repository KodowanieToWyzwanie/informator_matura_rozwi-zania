with open("dane6.txt", "r") as file:
    dane = file.read().split()

system_poz = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

for item in dane:
    item_list = map(int, list(item))
    system_poz[int(max(item_list)) + 1] += 1

print(system_poz)
