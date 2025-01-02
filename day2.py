"""
solves day 2
"""


def main():
    """
    check levels report safety
    """
    with open("./day2.txt", "r", encoding="utf-8") as file:
        input_data = file.readlines()

    def validate_reports(levels: list[int]):
        """
        validate report
        """
        diffs = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

        # preciso que seja all -1
        if all(diff > 0 and diff in range(1, 4) for diff in diffs) or all(
            diff < 0 and diff in range(-3, 0) for diff in diffs
        ):
            return True
        else:
            return False

    safe_reports = 0

    for line in input_data:
        level_list = [int(num.strip()) for num in line.split()]
        if validate_reports(level_list):
            safe_reports += 1
        else:
            # remove one report level at time to validate if
            # the report becomes safe
            for i in range(len(level_list)):
                temp_level_list = level_list.copy()
                temp_level_list.pop(i)
                if validate_reports(temp_level_list):
                    safe_reports += 1
                    break

    print(safe_reports)


if __name__ == "__main__":
    main()
