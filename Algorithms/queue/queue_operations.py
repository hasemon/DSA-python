from queue import Queue

maxsize = int(input("Enter maximum size of queue: "))
q = Queue(maxsize)

print('Enter elements of queue')
for i in range(maxsize):
    q.put(int(input()))

print('After popping: ')
print("Front is: ", q.queue[0])
print("Rear is: ", q.queue[-1])
print("Your queue is: ", q.queue)

x = input("Enter y to delete an element from queue: ")
if x == 'y':
    q.get()

print('After popping: ')
print("Front is: ", q.queue[0])
print("Rear is: ", q.queue[-1])

print("Your queue is: ", q.queue)