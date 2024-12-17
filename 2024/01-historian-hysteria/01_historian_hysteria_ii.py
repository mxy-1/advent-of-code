example_input = """\
3   4
4   3
2   5
1   3
3   9
3   3\
"""


def get_similarity_score(left_list: list, numbers_dict: dict) -> int:
    similarity_score = 0
    for i in range(len(left_list)):
        similarity_score += int(left_list[i]) * numbers_dict.get(left_list[i], 0)
    return similarity_score


def main(test_input: str) -> int:
    numbers_list = test_input.split()
    left_list = numbers_list[0::2]
    right_list = numbers_list[1::2]

    numbers_count = {}
    for number in set(right_list):
        numbers_count[number] = right_list.count(number)

    similarity_score = get_similarity_score(left_list, numbers_count)
    return similarity_score


if __name__ == "__main__":
    f = open("input.txt", "r")
    test_input = f.read()
    similarity_score = main(test_input)
    print(f'{similarity_score=}')
# similarity_score=22776016
