import plotly.express as px
import multiprocessing
import pandas as pd
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
    runs = 500000

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

    for k,v in full_dict.items(): #
        newvalue = {k : len(v)}
        full_dict.update(newvalue)
    print(f'Checkpoint 2:', round(time.time() - time_start,2), 'seconds')

    df = px.data.iris()
    df = pd.DataFrame.from_dict(full_dict, orient ='index', columns=["Number of steps"])
    df.index.names = ['Starting number']
    fig = px.scatter(df, y="Number of steps", color=df.index, title=str(f'{runs} runs done in {int(time.time() - time_start)} seconds 😁'))
    fig.show()

    print(f'Time taken for {runs} runs:', round(time.time() - time_start,2), 'seconds')
