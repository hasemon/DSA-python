numArrayLength = int(input('Enter array length: '))

numArray = []

print("Enter", numArrayLength, "elements: ")
for i in range(numArrayLength):
    numArray.append(int(input()))

print("Original array:", numArray)

for i in range(numArrayLength - 1):
    for j in range(numArrayLength - i - 1):
        if numArray[j] > numArray[j + 1]:
            numArray[j], numArray[j + 1] = numArray[j + 1], numArray[j]

print("Sorted array:", numArray)
