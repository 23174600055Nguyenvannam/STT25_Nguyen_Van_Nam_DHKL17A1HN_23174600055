import time
import threading

class SimpleTask:
    def run_stask(self):
        for i in range(1,4):
            print('đã in lần thứ :', i)
            time.sleep(1)

def main():
    task = [threading.Thread(target=SimpleTask().run_stask) for _ in range(4)]
    for i in task:
        i.start()
    for i in task:
        i.join()

if __name__ == "__main__":
    main()       