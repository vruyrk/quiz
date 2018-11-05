class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def is_empty(self):
        return len(self.queue) == 0

    def insert(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()

def main():
    myQueue = PriorityQueue()
    myQueue.insert(35)
    myQueue.insert(3)
    myQueue.insert(15)
    myQueue.insert(33)
    print(myQueue)
    while not myQueue.is_empty():
        myQueue.dequeue()
        print(myQueue)

main()