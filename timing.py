import atexit
from time import time, strftime, localtime
from datetime import timedelta


class Timing:
    start = None

    @classmethod
    def secondsToStr(cls, elapsed=None):
        if elapsed is None:
            return strftime("%Y-%m-%d %H:%M:%S", localtime())
        else:
            return str(timedelta(seconds=elapsed))

    @classmethod
    def log(cls, s, elapsed=None):
        line = "=" * 40
        print(line)
        print(cls.secondsToStr(), '-', s)
        if elapsed:
            print("Elapsed time:", elapsed)
        print(line)
        print()

    @classmethod
    def endlog(cls):
        end = time()
        elapsed = end - cls.start
        cls.log("End Program", cls.secondsToStr(elapsed))

    @classmethod
    def start_program(cls):
        start = time()
        atexit.register(cls.endlog)
        cls.log("Start Program")
