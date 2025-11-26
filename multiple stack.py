# Multiple Stack sederhana dalam satu list besar

data = []      # satu list untuk dua stack
stackA = []    # stack A
stackB = []    # stack B

# push ke stack A
def pushA(x):
    stackA.append(x)

# push ke stack B
def pushB(x):
    stackB.append(x)

# pop dari stack A
def popA():
    if stackA:
        return stackA.pop()
    return None

# pop dari stack B
def popB():
    if stackB:
        return stackB.pop()
    return None

# contoh penggunaan
pushA(10)
pushA(20)
pushB(5)
pushB(7)

print("Stack A:", stackA)
print("Stack B:", stackB)

print("Pop A:", popA())
print("Pop B:", popB())
