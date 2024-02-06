# delete algorithm
numArrayLength = int(input('Enter array length: '))

numArray = []

print("Enter", numArrayLength, "elements: ")
for i in range(numArrayLength):
    numArray.append(int(input()))

print("Original array:", numArray)

upperBound = numArrayLength - 1
location = int(input('Enter index location to delete: '))

while location < upperBound:
    numArray[location] = numArray[location + 1]
    location += 1

numArray.pop()

print("Array after deletion:", numArray)
