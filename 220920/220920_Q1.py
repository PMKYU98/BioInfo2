money = 17911
Coins = [1,3,5,7,11,13,19,20,22]

dicStack = {}
for coin in Coins:
    dicStack[coin] =1

for i in range(1,money+1):
    if i in dicStack: 
        continue
    else:
        dicStack[i] = i
        for j in range(1, i//2 +1):
            temp = dicStack[j] + dicStack[i-j]
            if temp < dicStack[i]: dicStack[i] = temp

print(dicStack)
print(dicStack[money])