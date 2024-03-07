def write_list(mwriter, my_list):
    """This function write all elements in the list"""
    for x in my_list:
        mwriter.write(f"{x} ")
    mwriter.write('\n')


with open('input14.txt') as reader, open('output14.txt', 'w') as writer:
    t = int(reader.readline())
    for i in range(1, t + 1):
        arr = [x for x in reader.readline().split()]
        arr.sort(reverse=False)  # sort elements in list asc
        writer.write(f'Test {i}:\n')
        write_list(writer, arr)
