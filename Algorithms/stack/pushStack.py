maxStk = int(input("Enter Top of stack: "))

stk = []
print('Enter elements of stack')
for i in range(maxStk):
    stk.append(int(input()))

print('Your stack is:', stk, 'and Top is:', len(stk))
