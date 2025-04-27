from threading import Thread, Condition, current_thread
import time


def printer_thread():
    global prime_holder
    global found_prime

    while not exit_prog:
        try:
            cond_var.acquire()
            while not found_prime and not exit_prog:
                cond_var.wait(timeout=0.1)

            if not exit_prog:
                value = prime_holder
                print(f"{current_thread().getName()} prints {value}")
                prime_holder = None
                found_prime = False
                cond_var.notify()  # Wake up finder thread
            cond_var.release()
        except Exception as e:
            print(f"Error in printer {current_thread().getName()}: {e}")

    print(f"printer {current_thread().getName()} exiting")


def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num < 2 or num % 2 == 0:
        return False
    div = 3
    while div <= int(num**0.5):
        if num % div == 0:
            return False
        div += 2
    return True


def finder_thread():
    global prime_holder
    global found_prime

    i = 1
    while not exit_prog:
        while not is_prime(i) and not exit_prog:
            i += 1

        if exit_prog:
            break

        try:
            cond_var.acquire()
            prime_holder = i
            found_prime = True
            cond_var.notify()  # Wake up one printer thread
            cond_var.release()

            cond_var.acquire()
            while found_prime and not exit_prog:
                cond_var.wait(timeout=0.1)
            cond_var.release()
        except Exception as e:
            print(f"Error in finder: {e}")

        i += 1

    print("finder exiting")


if __name__ == "__main__":
    cond_var = Condition()
    found_prime = False
    prime_holder = None
    exit_prog = False

    printerThread = Thread(target=printer_thread, name="Printer-1")
    printerThread.start()

    printerThread2 = Thread(target=printer_thread, name="Printer-2")
    printerThread2.start()

    printerThread3 = Thread(target=printer_thread, name="Printer-3")
    printerThread3.start()

    finderThread = Thread(target=finder_thread, name="Finder")
    finderThread.start()

    time.sleep(3)

    exit_prog = True

    try:
        cond_var.acquire()
        cond_var.notify_all()
        cond_var.release()
    except Exception as e:
        print(f"Error during shutdown: {e}")

    printerThread.join()
    printerThread2.join()
    printerThread3.join()
    finderThread.join()
