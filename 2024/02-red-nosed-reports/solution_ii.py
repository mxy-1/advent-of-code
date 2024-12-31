example_input = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9\
"""


def is_safe(report: list[str]) -> bool:
    """
    Args:
        report: ['7', '6', '4', '2', '1']
    """
    report = [int(report) for report in report]
    sorted_report = sorted(report)

    if sorted_report != report and sorted_report[::-1] != report:
        return False

    previous_level = report[0]
    for level in report[1:]:
        if level < previous_level - 3 or level > previous_level + 3 or level == previous_level:
            return False
        previous_level = level

    return True


def main(input: str) -> int:
    reports = input.splitlines()
    parsed_reports = list(report.split(" ") for report in reports)
    safe_reports = 0
    for parsed_report in parsed_reports:
        if is_safe(parsed_report):
            safe_reports += 1
        else:
            for i, level in enumerate(parsed_report):
                duplicate_parsed_report = parsed_report[:]
                del duplicate_parsed_report[i]
                if is_safe(duplicate_parsed_report):
                    safe_reports += 1
                    break

    return safe_reports


if __name__ == '__main__':
    f = open("input.txt", "r")
    input_str = f.read()
    total_safe_reports = main(input_str)
    print(f"{total_safe_reports=}")
    f.close()
