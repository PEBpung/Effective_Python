car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]

oldest, *others, youngest = car_ages

x = others[::2]
y = x[1:-1]
z = y[::-1]

print(z)

