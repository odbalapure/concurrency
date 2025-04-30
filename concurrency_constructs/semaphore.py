import threading
import time

TARGET_VALUE = 5000
semaphore = threading.Semaphore(5)  # Semaphore with a count of 5

# Global shared resource
counter = 0


def worker():
    global counter
    while True:
        semaphore.acquire()  # Acquire the semaphore
        if counter >= TARGET_VALUE:
            semaphore.release()  # Release the semaphore
            break
        counter += 1
        time.sleep(0.001)  # Simulate work
        semaphore.release()  # Release the semaphore


def main():
    start_time = time.time()

    workers = [threading.Thread(target=worker) for _ in range(10)]
    for w in workers:
        w.start()
    for w in workers:
        w.join()

    end_time = time.time()
    print("Time taken:", end_time - start_time, "seconds", counter)


if __name__ == "__main__":
    main()
