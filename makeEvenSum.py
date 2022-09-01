Numbers = [int(i) for i in input().split()]
Even= []
Count = 0
for i in range(len(Numbers)):
    if Numbers[i] %2 == 0 and Numbers[i] != 0:
        Even.append(Numbers[i])
for i in range(len(Even)):
    for j in range(i+1,len(Even)):
            if (Even[i] + Even[j] )% 2 == 0:
                Count += 1 
print(Count)    
print(Even)
print('Problem Not done yet')        