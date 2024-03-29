# Generator pipeline

def get_odd_numbers_squared_and_ending_in_1():
    """if number is odd, square that number,
    if the number ends in 1, print"""
    for n in range(1000):
        if n % 2 != 0:
            n **= 2
            if n % 10 == 1:
                print("Match found ---->{}".format(str(n)))


get_odd_numbers_squared_and_ending_in_1()

# Expand on the above function, separate into functional units as generators.

block = range(1000)


def square():
    """Square the number if odd and yield the result"""
    for n in range:
        yield n ** 2
    return result



