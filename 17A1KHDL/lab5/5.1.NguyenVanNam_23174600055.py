import time
class Simpletask:
    def run_task(self):
        for i in range(1,11):
            print("đã in lần thứ i", i)
            time.sleep(2)

def main():
    task = Simpletask()
    task.run_task()

if __name__ == "__main__":
    main()