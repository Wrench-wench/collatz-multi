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
    #print('The number', starting_number, 'has', len(steps_history), 'steps.')
    Q.put(step_dict)


# How to add a key and value in one line:
# step_dict['UniquekeyName'] = 'Value'

if __name__ == "__main__":
    time_start = time.time()

    runs = 1000000

    Q = multiprocessing.Queue()
    for run in range((runs + 1)):
        run = multiprocessing.Process(target=collatz, args=(run,))
        run.start()
        Q.get()
        run.join()

    print(f'Time taken for {runs} runs:', time.time() - time_start)

