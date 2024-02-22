arrayLength = int(input('Enter array length: '))

theArray = []

print('Enter the values of the array: ')
for i in range(arrayLength):
    theArray.append(int(input()))

print('The array is: ', theArray)

arrOperation = input('Enter array operation: i for insertion, d for deletion: ')

upperbound = arrayLength - 1

if arrOperation == 'i':
    newValue = int(input('Enter the value to insert: '))
    theArray.append(None)
    location = int(input(f'Enter location below: {arrayLength} to insert: '))

    while upperbound >= location:
        theArray[upperbound + 1] = theArray[upperbound]
        upperbound -= 1
    theArray[location] = newValue
    print('The new array after insert: ', theArray)
elif arrOperation == 'd':
    location = int(input(f'Enter location below: {arrayLength} to delete: '))
    while location < upperbound:
        theArray[location] = theArray[location + 1]
        location += 1
    theArray = theArray[:len(theArray) - 1]
    print('The new array after delete: ', theArray)
else:
    print('Enter currect operation.')
