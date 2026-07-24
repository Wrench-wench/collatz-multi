import multiprocessing
import time
import sys

runs = 100000000
chunk_size = 100000


def collatz(work):
    start, end = work

    try:
        for starting_number in range(start, end):
            assert starting_number > 1

            number = starting_number
            while number != 1:
                if (number % 2) == 0:
                    number = number // 2
                else:
                    number = (number * 3) + 1

            #if starting_number % 100000 == 0:
            #    print(f'Run number {starting_number}')
            #    print(f'Progress: {int((starting_number / runs) * 100)}%\n')

    except KeyboardInterrupt:
        pool.terminate()
        return False
    except AssertionError:
        pool.terminate()
        return False
    except MemoryError:
        pool.terminate()
        return False


if __name__ == "__main__":

    if runs > sys.maxsize:
        print(f'{runs} is not supported by this system, switching to largest number supported ({sys.maxsize}) instead.')
        runs = sys.maxsize

    time_start = time.time()
    print('Number of CPUs:', multiprocessing.cpu_count())
    print(f'Checkpoint 0:', round(time.time() - time_start, 2), 'seconds')

    work = []

    for start in range(2, runs, chunk_size):
        end = min(start + chunk_size, runs)
        work.append((start, end))

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        try:
            pool.map(collatz, work)
        except KeyboardInterrupt:
            pool.terminate()

    print(f'Checkpoint 1:', round(time.time() - time_start, 2), 'seconds')
    print(f'Time taken for {runs} runs:', time.time() - time_start, 'seconds')