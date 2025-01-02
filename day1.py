def main():
    with open("./day1.txt", "r", encoding="utf-8") as file:
        ids_input = file.readlines()

    first_list, second_list = [], []

    for line in ids_input:
        first_value, second_value = map(int, line.split())
        first_list.append(first_value)
        second_list.append(second_value)

    first_list.sort()
    second_list.sort()

    lists_total_difference = sum(
        abs(a - b)
        for a, b in zip(
            first_list,
            second_list,
        )
    )

    similarity_occurrences = {}
    for location_id in first_list:
        if location_id in second_list:
            similarity_occurrences[location_id] = (
                similarity_occurrences.get(location_id, 0) + 1
            )

        else:
            similarity_occurrences[location_id] = 1

    similarity_score = sum(
        location_id * similarity_occurrences.get(location_id, 0)
        for location_id in similarity_occurrences
    )

    print(f"lists_total_difference: {lists_total_difference}")
    print(f"similarity_score: {similarity_score}")


main()
