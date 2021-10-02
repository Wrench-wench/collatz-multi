import timeit

import_module = 'import multiprocessing'

code = """
#print('Number of CPUs:', multiprocessing.cpu_count())

def collatz(starting_number) -> dict:

    step_dict = {}
    steps = 0
    steps_history = []
    number = starting_number

    while number != 1:
        if (number % 2) == 0:
            number = number // 2
        else:
            number = (number * 3) + 1
        steps += 1
        steps_history.append(number)

    step_dict[starting_number] = steps_history
    Q.put(step_dict)


runs = 20
Q = multiprocessing.Queue()
for run in range(2,(runs + 1)): # Minimum for range must be 2
    run = multiprocessing.Process(target=collatz, args=(run,))
    run.start()
    Q.get()
    run.join()"""

starttime = timeit.default_timer()
print('Time taken for the first 20 numbers, 1 thousand times:', timeit.timeit(stmt=code, setup=import_module, number=1000))
print('Time taken:', round(((timeit.default_timer() - starttime) / 60),2), 'minutes')