import time
from hello_branch import hello
from real_branch import f

if __name__ == "__main__":
    counter = 0
    while counter < 1000:
        hello()
        f()
        counter += 1
        time.sleep(2)
