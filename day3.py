import re


def main():
    with open("./day3.txt", "r", encoding="utf-8") as file:
        patt = r"mul\((\d{1,3}),(\d{1,3})\)"
        total = 0

        for line in file:
            matches = re.finditer(patt, line)
            for match in matches:
                first_number, second_number = map(int, match.groups())
                total += first_number * second_number

        print(total)


if __name__ == "__main__":
    main()
