money = 40
Coins = [1,5,10,20,25,50]

dicStack = {1: 1, 5: 1, 10: 1, 20: 1, 25: 1, 50: 1}

for i in range(1,money+1):
    if i in dicStack: 
        continue
    else:
        dicStack[i] = i
        for j in range(1, i//2 +1):
            temp = dicStack[j] + dicStack[i-j]
            if temp < dicStack[i]: dicStack[i] = temp

print(dicStack[money])