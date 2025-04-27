###################################
# Creating threads
###################################

# Threads are created using the using the "Thread" class
# Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
# target: the code/function the thread being created will execute
# Arguments can be passed as a tuple "args" or dictionary using "kwargs"
# daemon: Is the thread daemon
from threading import Thread
from threading import current_thread


def thread_task(a, b, c, key1, key2):
    print(
        "{0} received the arguments: {1} {2} {3} {4} {5}".format(
            current_thread().getName(), a, b, c, key1, key2
        )
    )


my_thread = Thread(
    group=None,  # reserved
    target=thread_task,  # callable object
    name="demoThread",  # name of thread
    args=(1, 2, 3),  # arguments passed to the target
    kwargs={"key1": 777, "key2": 111},  # dictionary of keyword arguments
    daemon=None,  # set true to make the thread a daemon
)  # demoThread received the arguments: 1 2 3 777 111

my_thread.start()  # start the thread

my_thread.join()  # wait for a thread to finish executing before the main thread continues


###################################
# Subclassing the "Thread" class
###################################
class MyTask(Thread):
    def __init__(self):
        Thread.__init__(self, name="subclass_thread", args=(2, 3))

    def run(self):
        print(f"{current_thread().getName()} is executing")


subclass_thread = MyTask()
subclass_thread.start()
subclass_thread.join()

print(f"{current_thread().getName()} thread is exiting...")  # Main thread is exiting...
