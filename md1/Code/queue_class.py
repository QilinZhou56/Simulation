class Queue:

    def __init__(self):
        self.__queue = []

    def enqueue(self, value):
        self.__queue.append(value)

    def dequeue(self):
        return self.__queue.pop(0)

    def is_empty(self):
        return len(self.__queue) == 0

    def length(self):
        return len(self.__queue)

    def front(self):
        return self.__queue[0]

    def __repr__(self):
        s  = "FRONT\n"
        s += "-----\n"
        
        for v in self.__queue:
            s += str(v) + "\n"

        s += "----\n"
        s += "BACK\n"
        return s