def MutiplywithoutAstric(First,Second,Count,Result):
    if Second == Count:
        print(Result)
    else:
        Count = Count + 1
        Result = Result + First
        MutiplywithoutAstric(First,Second,Count,Result)
First = int(input("First Number:"))
Second = int(input("Second Number:"))   
Result = First
MutiplywithoutAstric(First,Second,1,Result)