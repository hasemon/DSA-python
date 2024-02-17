# pop operation in a stack

stk = []

maxstk = int(input("Enter maximum size of stack: "))
top = int(input("Enter Top of stack: "))

print("Before poping")
if top <= 0:
    print("Stack Underflow")
else:
    print("Enter elements of stack")
    for i in range(top):
        stk.append(int(input()))

    print("Your stack is:", stk, "and Top is:", top)

    stk = stk[:top - 1]
    top -= 1
    print("After poping")
    print("Your stack is:", stk, "and Top is:", top)
