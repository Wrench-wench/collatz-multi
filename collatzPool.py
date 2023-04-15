import multiprocessing
import time

def collatz(starting_number):

    step_dict = {}
    number = starting_number
    steps = 0
    steps_history = []

    try:
        assert starting_number > 1
    except AssertionError as a:
        steps_history.append(starting_number)
        step_dict[starting_number] = steps_history
        return

    while number != 1:
        if (number % 2) == 0:
            number = number // 2
        else:
            number = (number * 3) + 1
        steps += 1
        steps_history.append(number)

    step_dict[starting_number] = steps_history
    return steps_history

if __name__ == "__main__":
    time_start = time.time()
    print('Number of CPUs:', multiprocessing.cpu_count())
    print(f'Checkpoint 0:', round(time.time() - time_start, 2), 'seconds')
    coll_list = []
    coll_dict = {}
    runs = 1000000

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        coll_dict[runs] = pool.map(collatz, range(runs))

    print(f'Checkpoint 1:', round(time.time() - time_start, 2), 'seconds')

    # Do something with the information

    print(f'Checkpoint 2:', round(time.time() - time_start, 2), 'seconds')
    print(f'Time taken for {runs} runs:', time.time() - time_start)