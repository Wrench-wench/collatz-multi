import multiprocessing
import time

print('Number of CPUs:', multiprocessing.cpu_count())

def collatz(starting_number) -> dict:

    step_dict = {}
    number = starting_number
    steps = 0
    steps_history = []

    try:
        assert starting_number > 1
    except AssertionError as a:
        steps_history.append(starting_number)
        step_dict[starting_number] = steps_history
        Q.put(step_dict)
        return

    while number != 1:
        if (number % 2) == 0:
            number = number // 2
        else:
            number = (number * 3) + 1
        steps += 1
        steps_history.append(number)

    step_dict[starting_number] = steps_history
    Q.put(step_dict)

if __name__ == "__main__":
    time_start = time.time()
    print(f'Checkpoint 0:', round(time.time() - time_start,2), 'seconds')
    dict_list = []
    runs = 1000

    Q = multiprocessing.Queue()
    for run in range(2,(runs + 1)):
        dict_name = f'run-{run}'
        run = multiprocessing.Process(target=collatz, args=(run,))
        run.start()
        dict_name = Q.get()
        dict_list.append(dict_name)
        run.join()
    print(f'Checkpoint 1:', round(time.time() - time_start,2), 'seconds')

    full_dict = {}
    for dict in dict_list:
        full_dict = {**full_dict, **dict} # Shallow merge two dicts: z = {**x, **y}

    for k,v in full_dict.items():
        print(k,':', len(v))
    print(f'Checkpoint 2:', round(time.time() - time_start,2), 'seconds')
    print(f'Time taken for {runs} runs:', time.time() - time_start)
