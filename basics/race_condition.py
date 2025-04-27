from threading import Thread, Lock
import sys


class Counter:
    def __init__(self):
        self.count = 0
        self.lock = Lock()

    def increment(self):
        for _ in range(100000):
            self.lock.acquire()
            self.count += 1
            self.lock.release()


if __name__ == "__main__":
    sys.setswitchinterval(0.005)

    num_threads = 5
    threads = [0] * num_threads
    counter = Counter()

    for i in range(0, num_threads):
        threads[i] = Thread(target=counter.increment)

    for i in range(0, num_threads):
        threads[i].start()

    for i in range(0, num_threads):
        threads[i].join()

    if counter.count != 500000:
        print(
            " If this line ever gets printed, "
            + "the author is a complete idiot and "
            + "you should return the course for a full refund!"
        )
    else:
        print(" count = {0}".format(counter.count))
