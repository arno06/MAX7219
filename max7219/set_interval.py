import time, threading


def set_interval(interval):
    def outer_wrap(function):
        def wrap(*args, **kwargs):
            def inner_wrap():
                while True:
                    time.sleep(interval)
                    function(*args, **kwargs)
            threading.Timer(0, inner_wrap).start()
        return wrap
    return outer_wrap