import multiprocessing

print('Number of CPUs:', multiprocessing.cpu_count())


def collatz(starting_number) -> dict:
    assert starting_number > 1

    step_dict = {}
    number = starting_number
    steps = 0
    steps_history = []

    while number != 1:

        if (number % 2) == 0:
            number = number // 2
        else:
            number = (number * 3) + 1
        steps += 1
        steps_history.append(number)

    step_dict[starting_number] = steps_history
    return step_dict


# How to add a key and value in one line:
# step_dict['UniquekeyName'] = 'Value'

runs = 30

while runs > 2:
    run = collatz(runs)
    steps = (next(iter(run.items())))

    # Print results
    print('Result for the number', next(iter(run)), 'Number of steps', len(steps[1]))
    runs += -1
