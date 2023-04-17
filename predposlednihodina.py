#thread
from time import sleep,perf_counter
from threading import Thread
from multiprocessing import Process

beh_pocitace = perf_counter()
print(beh_pocitace)
def funkce1():
    # print("start",vlakno,"vlakna")
    # sleep(1)
    # print("konec",vlakno,"vlakna")
    print("start vlakna")
    sleep(1)
    print("konec vlakna")




# threads = []
# for n in range(1,11):
#     thread = Thread(target=funkce1,args=(n,))
#     thread.start()
#     threads.append(thread)
# for x in threads:
#     thread.join()

# thread1 = Thread(target=funkce1,args=(1,))
# thread2 = Thread(target=funkce1,args=(2,))

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()





# beh_pocitace = perf_counter()
# print(beh_pocitace)


if __name__ == "__main__":

    beh_pocitace = perf_counter()
    print(beh_pocitace)

    proces1 = Process(target=funkce1)
    proces2 = Process(target=funkce1)
    proces1.start()
    proces2.start()

    proces1.join()
    proces2.join()

    beh_pocitace = perf_counter()
    print(beh_pocitace)