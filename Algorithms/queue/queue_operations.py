from queue import Queue

maxsize = int(input("Enter maximum size of queue: "))
q = Queue(maxsize)

print('Enter elements of queue')
for i in range(maxsize):
    q.put(int(input()))

print("Your queue is: ", q.queue)

x = input("Enter y to delete element from queue: ")
if x == 'y':
    q.get()

print("Your queue is: ", q.queue)