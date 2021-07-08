def remainder(number, divisor):
    return number % divisor

my_kwargs = {
    'number': 20,
}

other_kwargs = {
    'divisor': 7,
}

assert remainder(**my_kwargs, **other_kwargs) == 6

