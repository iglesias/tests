import multiprocessing
import time

def worker():
    """worker function"""
    print 'Worker'
    time.sleep(10)

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()
