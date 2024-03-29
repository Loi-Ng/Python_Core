def draw_heart(width, height):
    heart = []
    for i in range(1, height + 1):
        heart.append([])
        for j in range(1, width + 1):
            if (i == 1 and j != 1 and j != 4 and j != 7) or \
                    (i == 2 or i == 3) or \
                    (i == 4 and j != 1 and j != 7) or \
                    (i == 5 and 3 <= j <= 5) or \
                    (i == 6 and j == 4):
                heart[i - 1].append(' * ')
            else:
                heart[i - 1].append('   ')
    return heart


def writer_heart(matrix):
    """Hàm hiển thị các phần tử trong ma trận"""
    with open('output27.txt', 'w') as writer:
        for x in matrix:
            for e in x:
                writer.write(f'{e}')
            writer.write('\n')


result = draw_heart(7, 6)
writer_heart(result)
