import multiprocessing

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
        return step_dict

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

if __name__ == "__main__":

    for run in range(2,31):
        run = multiprocessing.Process(target=collatz, args=(run,))
        run.start()

