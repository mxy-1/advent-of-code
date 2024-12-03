example_input = """\
3   4
4   3
2   5
1   3
3   9
3   3\
"""


def main(test_input):
    numbers_list = test_input.split()
    left_list = sorted(numbers_list[0::2])
    right_list = sorted(numbers_list[1::2])

    total_distance = 0

    for i in range(len(left_list)):
        total_distance += abs(int(left_list[i]) - int(right_list[i]))

    return total_distance

if __name__ == "__main__":
    f = open("input.txt", "r")
    test_input = f.read()
    total_distance = main(test_input)
    print(f'{total_distance=}')
