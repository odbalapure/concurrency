from threading import current_thread, Lock, Thread
import time


def increment(lock1: Lock, lock2: Lock):
    lock1.acquire()
    print(current_thread().getName() + " acquired lock 1")
    time.sleep(1)
    lock2.acquire()
    print(current_thread().getName() + " got both the locks")


def deccrement(lock1: Lock, lock2: Lock):
    lock2.acquire()
    print(current_thread().getName() + " acquired lock 2")
    time.sleep(1)
    lock1.acquire()
    print(current_thread().getName() + " got both the locks")


if __name__ == "__main__":
    lock1, lock2 = Lock(), Lock()
    Thread(target=increment, args=(lock1, lock2), name="Thread 1").start()
    Thread(target=deccrement, args=(lock1, lock2), name="Thread 2").start()

# Thread 1 acquired lock 1
# Thread 2 acquired lock 2
# Execution Timed Out!
