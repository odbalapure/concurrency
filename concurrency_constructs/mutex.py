import threading
import time

counter = 0
lock = threading.Lock()


def increment_counter_with_mutex():
    global counter
    for _ in range(100):
        with lock:
            temp = counter
            time.sleep(0.001)
            counter = temp + 1


def increment_counter_with_no_mutex():
    global counter
    for _ in range(100):
        temp = counter
        time.sleep(0.001)
        counter = temp + 1


def run_experiment(experiment_name, task):
    global counter
    counter = 0  # reset before each run

    t1 = threading.Thread(target=task)
    t2 = threading.Thread(target=task)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"Final counter value of '{experiment_name}': {counter}")


if __name__ == "__main__":
    run_experiment("With Mutex", increment_counter_with_mutex)
    run_experiment("No Mutex", increment_counter_with_no_mutex)
