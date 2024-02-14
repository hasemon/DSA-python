stk = []

maxstk = int(input("Enter maximum size of stack: "))
top = int(input("Enter Top of stack: "))

print("Before pushing")
if top >= maxstk:
    print("Stack Overflow")
else:
    print("Enter elements of stack")
    for i in range(top):
        stk.append(int(input()))

    print("Your stack is:", stk, "and Top is:", top)
    item = int(input("Enter item to be pushed: "))
    stk += [None]
    stk[top] = item
    top += 1
    print("After pushing")
    print("Your stack is:", stk, "and Top is:", top)
