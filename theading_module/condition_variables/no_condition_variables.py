# W/o conditions we need to keep polling for a "predicate"
# One issue with this program is that we are not using any locks
# Another also we are constantly polling the "found_prime" to be true
# This is called as busy waiting as it wastes CPU cycles
# Ideally the "printer" thread should go to sleep until "found_prime" becomes true

from threading import Thread
import time

# This is a very crude implementation of a producer & consumer problem
# The printer is the "consumer" & finder is the "producer"
# Even if we did use Locks there they won't help us singal the "consumer"
# NOTE: This solution won't work for more than 2 threads


def printer_thread_func():
    global prime_holder
    global found_prime

    while not exit_prog:
        while not found_prime and not exit_prog:
            time.sleep(0.1)

        if not exit_prog:
            print(prime_holder)

            prime_holder = None
            found_prime = False


def is_prime(num):
    if num == 2 or num == 3:
        return True

    div = 2

    while div <= num / 2:
        if num % div == 0:
            return False
        div += 1

    return True


def finder_thread_func():
    global prime_holder
    global found_prime

    i = 1

    while not exit_prog:

        while not is_prime(i):
            i += 1

        prime_holder = i
        found_prime = True

        while found_prime and not exit_prog:
            time.sleep(0.1)

        i += 1


found_prime = False
prime_holder = None
exit_prog = False

printer_thread = Thread(target=printer_thread_func)
printer_thread.start()

finder_thread = Thread(target=finder_thread_func)
finder_thread.start()

# Let the threads run for 3 seconds
time.sleep(3)

# Let the threads exit
exit_prog = True

printer_thread.join()
finder_thread.join()
