numArrayLength = int(input('Enter array length: '))

numArray = []

print("Enter", numArrayLength, "elements: ")
for i in range(numArrayLength):
    numArray.append(int(input()))

print("Original array:", numArray)

searchValue = int(input('Enter value to search: '))
numArray.append(searchValue)

location = 0
numArrayIndex = []

found = False
for location in range(numArrayLength):
    numArrayIndex.append(location)
    if searchValue == numArray[-1]:
        found = True
        break


print('Index array: ', numArrayIndex)
print('New array: ', numArray)

if found:
    print(searchValue, "found in the Array")
else:
    print(searchValue, "not found")
