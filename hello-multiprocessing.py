import multiprocessing, os, time, signal, sched

def execute():
    print '{}: new process started'.format(os.getpid())
    try:
        while True:
            print '{}: polling'.format(os.getpid())
            time.sleep(1)
    finally:
        print '{}: process ended'.format(os.getpid())


class Poller(multiprocessing.Process):

    def __init__(self):
        super(Poller, self).__init__()

    def run(self):
        execute()

if __name__ == '__main__':
    print '{}: main'.format(os.getpid())
    p1 = Poller()
    p2 = Poller()
    pool = multiprocessing.Pool()
    try:
        p1.start()
        p2.start()
        p1.join()
        p2.join()
    finally:
        print '{}: main end'.format(os.getpid())
