import time
from contextlib import contextmanager


class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
        print(f"time: {self.elapsed_time:.1f}")


@contextmanager
def cm_timer_2():
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"time: {elapsed_time:.1f}")


def test_timer():
    print("Testing cm_timer_1 (class-based):")
    with cm_timer_1():
        time.sleep(2.5)

    print("\nTesting cm_timer_2 (contextlib-based):")
    with cm_timer_2():
        time.sleep(1.5)
