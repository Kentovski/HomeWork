# /usr/bin/python3

# MELNIKOV ILYA

count = 0


def max_sum(pyramid, row=0, column=0, sum=0):
    global count
    count += 1

    if row == len(pyramid) - 1:
        return sum + pyramid[row][column]

    return max(max_sum(pyramid, row + 1, column, sum + pyramid[row][column]),
               max_sum(pyramid, row + 1, column + 1, sum + pyramid[row][column]))


if __name__ == '__main__':
    pyramid_1 = [[7],
                 [2, 3],
                 [3, 3, 1],
                 [3, 1, 5, 4],
                 [3, 1, 3, 1, 3],
                 [2, 2, 2, 2, 2, 2],
                 [5, 6, 4, 5, 6, 4, 3]]

    pyramid_2 = [[1],
                 [2, 1],
                 [1, 2, 1],
                 [1, 2, 1, 1],
                 [1, 2, 1, 1, 1],
                 [1, 2, 1, 1, 1, 1],
                 [1, 2, 1, 1, 1, 1, 9]]

    print('Max sum for pyramid 1 - ' + str(max_sum(pyramid_1)))
    print('Max sum for pyramid 2 - ' + str(max_sum(pyramid_2)))
