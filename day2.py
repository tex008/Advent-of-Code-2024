"""
solves day 2
"""

with open("./day2.txt", "r", encoding="utf-8") as file:
    input_data = file.readlines()


def validate_reports(levels: list[int]):
    """
    validate report
    """
    diffs = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]
    if all(diffs > 0 and diffs in range(1, 4) for diffs in diffs) or all(
        diffs < 0 and diffs in range(-3, 0) for diffs in diffs
    ):
        return True
    else:
        return False


safe_reports = 0

for line in input_data:
    level_list = [int(num.strip()) for num in line.split()]
    if validate_reports(level_list):
        safe_reports += 1

print(safe_reports)
