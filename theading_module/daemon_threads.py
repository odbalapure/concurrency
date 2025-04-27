from threading import Thread
from threading import current_thread
import time


def regular_thread_task():
    while True:
        print("{0} executing".format(current_thread().getName()))
        time.sleep(1)


regular_thread = Thread(target=regular_thread_task, name="regular_thread", daemon=True)
regular_thread.start()  # start the regular thread
regular_thread.join()  # wait for the thread to finish

print("Main thread exiting but Python program doesn't")

# daemon=False + .join() => infinte loop continues and main thread never exits
# daemon=False + "no" .join() => infinte loop continues even when main exits
# daemon=True + .join() => infinte loop continues and main thread never exits
# daemon=True + "no" .join() => regular_thread will exit as soon as main exits
