import time
from numba import njit, prange

runs = 9223372036854775807


@njit(parallel=True, fastmath=True, cache=True)
def collatz(runs):

    for starting_number in prange(2, runs):

        number = starting_number

        while number != 1:
            if number & 1:
                if number > 3074457345618258602:
                    break
                number = number * 3 + 1
            else:
                number >>= 1


if __name__ == "__main__":

    time_start = time.time()

    print(f'Checkpoint 0:', round(time.time() - time_start, 2), 'seconds')

    collatz(runs)

    print(f'Checkpoint 1:', round(time.time() - time_start, 2), 'seconds')
    print(f'Time taken for {runs} runs:', time.time() - time_start, 'seconds')