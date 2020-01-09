# Paralelo vs. Concurrente


import os
import time
# hilos y multiprocesamiento
import threading
import multiprocessing


def get_names_tuple():
    """ Return tuple with values for prints in mothods
        (id prosses, prosses name, thread name) """
    return (os.getpid(),
            multiprocessing.current_process().name,
            threading.current_thread().name
            )


def only_sleep():
    """ Do nothing, wait for a timer to expire """
    print("PID: %s, Process Name: %s, Thread Name: %s" % get_names_tuple())
    time.sleep(1)


def crunch_numbers():
    """ Do some computations """
    print("PID: %s, Process Name: %s, Thread Name: %s" % get_names_tuple())
    [x for x in range(10000000)]


#

def generic(start_time, target, iterator):
    # Run tasks serially
    [target() for _ in iterator]
    print("Serial time=", time.time() - start_time)


def generic2(start_time, iterator, type):
    # Run tasks using threads/processes
    [x.start() for x in iterator]
    [x.join() for x in iterator]
    print("{0} time={1}".format(type, time.time() - start_time))

#


def get_threads_list(target, NUM_WORKERS):
    return [threading.Thread(target=target) for _ in range(NUM_WORKERS)]


def get_processes_list(target, NUM_WORKERS):
    return [multiprocessing.Process(target=target) for _ in range(NUM_WORKERS)]


if __name__ == '__main__':
    multiprocessing.freeze_support()
    NUM_WORKERS = 1
    generic(time.time(), only_sleep, range(NUM_WORKERS))
    #
    threads = get_threads_list(only_sleep, NUM_WORKERS)
    processes = get_processes_list(only_sleep, NUM_WORKERS)
    generic2(time.time(), threads, 'Threads')
    generic2(time.time(), processes, 'Parallel')
