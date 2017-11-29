import threading
import time

class Worker(threading.Thread):
    """worker class"""

    def run(self):
        """run function"""
        print 'Worker'
        time.sleep(10)

if __name__ == '__main__':
    for i in range(5):
        Worker().start()
