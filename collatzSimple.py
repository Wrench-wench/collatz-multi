#####################################################################
#                                                                   #
#   Don't use this script, it wasn't written efficently correctly   #
#   Use the collatzPool.py file instead.                            #
#                                                                   #
#####################################################################


import multiprocessing
import time

def collatz(starting_number: int):

    step_dict = {}
    number = starting_number
    steps = 0
    steps_history = []

    try:
        assert starting_number > 1
    except AssertionError as a:
        return

    while number != 1:
        if (number % 2) == 0:
            number = number // 2
        else:
            number = (number * 3) + 1
        steps += 1
        steps_history.append(number)

    step_dict[starting_number] = steps_history
    return

if __name__ == "__main__":
    time_start = time.time()
    print(f'Checkpoint 0:', round(time.time() - time_start, 2), 'seconds')
    print('Number of CPUs:', multiprocessing.cpu_count())
    dict_list = []
    runs = 100

    Q = multiprocessing.SimpleQueue()
    for run in range(2,(runs + 1)):
        dict_name = f'run-{run}'
        run = multiprocessing.Process(target=collatz, args=(run,))
        run.start()
    print(f'Checkpoint 1:', round(time.time() - time_start,2), 'seconds')

#    full_dict = {}
#    for dict in dict_list:
#        full_dict = {**full_dict, **dict} # Shallow merge two dicts: z = {**x, **y}
#
#    for k,v in full_dict.items():
#        print(k,':', len(v))
    Q.close()
    print(f'Checkpoint 2:', round(time.time() - time_start,2), 'seconds')
    print(f'Time taken for {runs} runs:', time.time() - time_start)