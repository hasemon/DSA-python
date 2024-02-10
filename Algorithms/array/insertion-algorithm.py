# insertion algorithm
numArrayLength = int(input('Enter array length: '))

numArray = []

print("Enter", numArrayLength, "elements: ")
for i in range(numArrayLength):
    numArray.append(int(input()))

print("Original array:", numArray)


upperBound = numArrayLength - 1
location = int(input('Enter location to insert: '))
newValue = int(input('Enter new value: '))

numArray.append(0)

while upperBound >= location:
    numArray[upperBound + 1] = numArray[upperBound]
    upperBound -= 1

numArray[location] = newValue

print("Array after insertion:", numArray)
