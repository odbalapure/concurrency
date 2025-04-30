import threading

current_thread = threading.current_thread


def work():
    print(f"Thread {current_thread().name} is waiting at the barrier")
    barrier.wait()
    print(f"{current_thread().name} is released")


def barrier_action():
    print(f"All threads have reached the barrier")


if __name__ == "__main__":
    barrier = threading.Barrier(2, action=barrier_action)

    t1 = threading.Thread(target=work)
    t2 = threading.Thread(target=work)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
