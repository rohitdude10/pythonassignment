given_list = [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

max_ones = []
count_ones = 0
for i in range(len(given_list)):

    if given_list[i] == 1:
        count_ones = count_ones + 1
    if (given_list[i] == 0) or (i == len(given_list) - 1):
        max_ones.append(count_ones)
        count_ones = 0

print(max(max_ones))
