import multiprocessing
import time
import sys

runs = 10000000

def collatz(starting_number):
    #print(f'Run number {starting_number}')
    try:
        assert starting_number > 1

        number = starting_number
        while number != 1:
            if (number % 2) == 0:
                number = number // 2
            else:
                number = (number * 3) + 1

        #if starting_number % 100000 == 0:
        #    print(f'Run number {starting_number}\nProgress: {int((starting_number / runs) * 100)}% \n')
        #return True

    except KeyboardInterrupt as k:
        return False
    except AssertionError as a:
        return False
    except MemoryError as m:
        return False


if __name__ == "__main__":

    if runs > sys.maxsize:
        print(f'{runs} is not supported by this system, switching to largest number supported ({sys.maxsize}) instead.')
        runs = sys.maxsize

    time_start = time.time()
    print('Number of CPUs:', multiprocessing.cpu_count())
    print(f'Checkpoint 0:', round(time.time() - time_start, 2), 'seconds')

    #for num in range(runs):
    #    collatz(num)
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        try:
            pool.map(collatz, range(1, runs))
        except KeyboardInterrupt as k:
            pass

    print(f'Checkpoint 1:', round(time.time() - time_start, 2), 'seconds')
    print(f'Time taken for {runs} runs:', time.time() - time_start)