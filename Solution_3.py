def find_difference_in_column(lines, index_col, minuend_col, subtrahend_col):
    smallest_difference = None
    smallest_index = ""

    for index, line in enumerate(lines):
        split_line = line.split()
        if len(split_line) < max(minuend_col, subtrahend_col) or index == 0:
            continue
        key = split_line[index_col]
        minuend = float(split_line[minuend_col].replace("*", ""))
        subtrahend = float(split_line[subtrahend_col].replace("*", ""))
        difference = abs(minuend - subtrahend)
        if smallest_difference == None or difference < smallest_difference:
            smallest_difference = difference
            smallest_index = key

    return smallest_index, smallest_difference


def find_smallest_temp_spread(filepath):
    with open(filepath, "r") as file:
        lines = file.readlines()
        smallest_spread_temp_day, smallest_spread_temp = find_difference_in_column(
            lines, 0, 1, 2
        )

    return smallest_spread_temp_day, smallest_spread_temp


def find_smallest_goal_difference(filepath):
    with open(filepath, "r") as file:
        lines = file.readlines()
        football_team, smallest_goal_diff = find_difference_in_column(lines, 1, 6, 8)

    return football_team.replace("_", " "), smallest_goal_diff


if __name__ == "__main__":
    path = "./weather.dat"
    day, temp = find_smallest_temp_spread(path)
    print(f"Day {day} had the smallest temperature spread of {temp}")

    path = "./football.dat"
    team_name, diff = find_smallest_goal_difference(path)
    print(
        f"Team {team_name} had the smallest goal difference between FOR and AGAINST with {diff}"
    )
