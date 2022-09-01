Coins = [int(i) for i in input().split()]
TotalValue = Coins[0]*1 + Coins[1]*2
if (Coins[0] == 0 and Coins[1] % 2 == 0):
        print("YES")
elif (Coins[0] == 0 and Coins[1] % 2 != 0):
        print("NO")
elif (TotalValue % 2 == 0):
        print("YES")
else:
        print("NO")