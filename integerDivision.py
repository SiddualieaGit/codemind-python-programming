Value = int(input())
Value = (Value/10)
if Value > 0:
    Value = int(Value)
else:
    if round(Value) == int(Value):
        Value = Value - 1
    else:
        Value = round(Value)
print(Value)
print('code not completed yet')
