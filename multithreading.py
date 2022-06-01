from threading import Thread

if __name__ == "__main__":
    threads = []
    num_threads = 10

def square_numbers():
    for i in range(100):
        i*i

for i in range(num_threads):
    thread = Thread(target=square_numbers)
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()