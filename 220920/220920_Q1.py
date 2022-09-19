money = 40
Coins = [1,5,10,20,25,50]


def ADD_COIN(dicWallet, coin):
    dicWallet[coin] += 1

    if dicWallet[1] == 5:
        dicWallet[1] = 0
        dicWallet[5] += 1
    if dicWallet[5] == 2:
        dicWallet[5] = 0
        dicWallet[10] += 1
    if dicWallet[10] == 2:
        dicWallet[10] = 0
        dicWallet[20] += 1
    if dicWallet[20] >= 1 and dicWallet[5] >= 1:
        dicWallet[25] += 1
        dicWallet[20] -= 1
        dicWallet[5] -= 1
    if dicWallet[25] == 2:
        dicWallet[50] += 1
        dicWallet[25] -= 1

    return dicWallet

dicWallet = {1: 0, 5: 0, 10: 0, 20: 0, 25: 0, 50: 0}
for i in range(money):
    dicWallet = ADD_COIN(dicWallet, 1)

print(dicWallet)