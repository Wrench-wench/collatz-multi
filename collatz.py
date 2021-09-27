import multiprocessing

print('Number of CPUs:', multiprocessing.cpu_count())


def collatz(numberloops):

    steplist = []
    number = 0
    steps = 0

    while number != 1:

                if (number % 2) == 0:                  # If the number is even, divide it by two.
                    number = number // 2               # Integer division where the remainder is discarded: //
                    steplist.append(number)            # The operation yields an int instead of a float
                    steps += 1

                else:                                  # If the number is odd, triple it and add one.
                    number = (number * 3) + 1
                    steplist.append(number)
                    steps += 1


    print(steplist)

collatz(10)