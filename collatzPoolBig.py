import multiprocessing
import time

def collatz(starting_number):
    try:
        assert starting_number > 1
    except AssertionError as a:
        return

    number = starting_number
    while number != 1:
        if (number % 2) == 0:
            number = number // 2
        else:
            number = (number * 3) + 1
    return

if __name__ == "__main__":
    time_start = time.time()
    runs = 100
    print('Number of CPUs:', multiprocessing.cpu_count())
    print(f'Checkpoint 0:', round(time.time() - time_start, 2), 'seconds')

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.map(collatz, range(runs))

    print(f'Checkpoint 1:', round(time.time() - time_start, 2), 'seconds')
    print(f'Time taken for {runs} runs:', time.time() - time_start)