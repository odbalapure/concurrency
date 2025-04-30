import threading
import time

# NOTE:
# Lock/RLock cannot simulate true read/write behavior
# We can use an external library like "readerwriterlock"
# from readerwriterlock import rwlock
# rw_lock = rwlock.RWLockFair()
# rw_lock.gen_wlock()
# rw_lock.gen_rlock()

counter = 0
TARGET_VALUE = 1000
lock = threading.Lock()


def increment_value():
    global counter
    with lock:
        time.sleep(0.001)
        if counter <= TARGET_VALUE:
            counter += 1
    return counter


def read_value():
    global counter
    with lock:
        time.sleep(0.001)
        return counter


# These makes the reader/writer threads keep running
# This burns CPU cycle constantly
# The threads will stay alive but inefficiently
# def reader():
#     while True:
#         if read_value() > TARGET_VALUE:
#             break
#
# def writer():
#     while True:
#         if increment_value() > TARGET_VALUE:
#             break


# This approach allows OS to run other threads
# This is more CPU friendly
def reader():
    while read_value() < TARGET_VALUE:
        time.sleep(0.001)


def writer():
    while increment_value() < TARGET_VALUE:
        time.sleep(0.001)


if __name__ == "__main__":
    start = time.time()
    readers = [threading.Thread(target=reader) for _ in range(8)]
    writers = [threading.Thread(target=writer) for _ in range(2)]

    for t in readers + writers:
        t.start()

    for t in readers + writers:
        t.join()

    end = time.time()
    print(f"Final counter: {counter}")
    print(f"Time taken: {end - start} seconds")
