Sides = [int(i) for i in input().split()]

if (Sides[0]==10 and Sides[1]==0) or Sides[0]==0 and Sides[1]==10 :
    print("Yes")
elif (Sides[0]  + 1==Sides[1]) or (Sides[0]  - 1==Sides[1]) :
    print("Yes")
else:
    print("No")