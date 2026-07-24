import multiprocessing
import time
import sys

runs = 100000000
chunk_size = 100000


def collatz(work):
    start, end = work

    for starting_number in range(start, end):

        number = starting_number
        while number != 1:
            if (number & 1) == 0:
                number >>= 1
            else:
                number = (number * 3) + 1


if __name__ == "__main__":

    if runs > sys.maxsize:
        print(f'{runs} is not supported by this system, switching to largest number supported ({sys.maxsize}) instead.')
        runs = sys.maxsize

    time_start = time.time()
    print('Number of CPUs:', multiprocessing.cpu_count())
    print(f'Checkpoint 0:', round(time.time() - time_start, 2), 'seconds')

    work = (
        (start, min(start + chunk_size, runs))
        for start in range(2, runs, chunk_size)
    )

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.map(collatz, work)

    print(f'Checkpoint 1:', round(time.time() - time_start, 2), 'seconds')
    print(f'Time taken for {runs} runs:', time.time() - time_start, 'seconds')