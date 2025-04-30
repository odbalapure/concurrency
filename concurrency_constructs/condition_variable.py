import threading

shared_number = 0
ready = False
mtx = threading.Lock()
cv = threading.Condition(mtx)


def producer():
    global ready, shared_number
    with cv:
        shared_number = 100
        ready = True
        print(f"Producer has produced {shared_number}")
        cv.notify()


def consumer():
    with cv:
        cv.wait_for(lambda: ready)
        print(f"Consumer has consumed {shared_number}")


def main():
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()


if __name__ == "__main__":
    main()
