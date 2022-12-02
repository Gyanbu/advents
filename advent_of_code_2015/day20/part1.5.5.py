from multiprocessing import Process

import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True


q = 34000000
num_of_threads = 12


def presents_in_house(n):
    gifts_received = n * 10
    for i in range(n // 2):
        if n % (i + 1) == 0:
            gifts_received += (i + 1) * 10
    return gifts_received


def thread_pih(o, w):
    n = 65500
    while True:
        n += 1
        # if not is_prime(n):
        #     continue
        presents = presents_in_house(o * n + w)
        if presents >= q:
            print(f'[!!!{o * n + w}!!!]: {presents}')
            # with open(f'num{o}.txt', 'wt') as f:
            #     f.write(f'[!!!{o * n + w}!!!]: {presents}')
            return presents
        # print(f'[{o * n + w}]: {presents}')
        if n > 65520:
            return


if __name__ == '__main__':
    jobs = []
    # num_of_threads = 1
    for p in range(num_of_threads):
        process = Process(target=thread_pih, args=(num_of_threads, p))
        jobs.append(process)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()
