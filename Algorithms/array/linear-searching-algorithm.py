numArrayLength = int(input('Enter array length: '))

numArray = []

print("Enter", numArrayLength, "elements: ")
for i in range(numArrayLength):
    numArray.append(int(input()))

print("Original array:", numArray)

searchValue = int(input('Enter value to search: '))

location = 0
found = False
numArrayIndex = []


while location < numArrayLength:
    if numArray[location] == searchValue:
        found = True
        break
    else:
        location += 1

numArray.append(searchValue)

for i in range(len(numArray)):
    numArrayIndex.append(i)


print('Index array: ', numArrayIndex)
print('Orginal array: ', numArray)

if found:
    print(searchValue, "found at location: ", location)
else:
    print(searchValue, "not found")
