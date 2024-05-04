def find_smallest_temp_spread(filepath):
    with open(filepath, "r") as file:

        lines = file.readlines()
        smallest_spread_temp = None
        smallest_spread_temp_day = ""

        for single_line in lines:
            split_line = single_line.split()
            if len(split_line) == 0 or split_line[0] == "Dy":
                continue
            day = split_line[0]
            max_temp = float(split_line[1].replace("*", ""))
            min_temp = float(split_line[2].replace("*", ""))
            spread_temp = max_temp - min_temp
            if smallest_spread_temp == None or spread_temp < smallest_spread_temp:
                smallest_spread_temp = spread_temp
                smallest_spread_temp_day = day

    return smallest_spread_temp_day, smallest_spread_temp


def find_smallest_goal_difference(filepath):
    with open(filepath, "r") as file:

        lines = file.readlines()
        smallest_goal_diff = None
        football_team = ""

        for single_line in lines:
            split_line = single_line.split()
            if len(split_line) == 0 or split_line[0] == "Team" or "-" in split_line[0]:
                continue
            team_name = split_line[1]
            for_goals = int(split_line[6])
            against_goals = int(split_line[8])
            goal_diff = abs(for_goals - against_goals)
            if smallest_goal_diff == None or goal_diff < smallest_goal_diff:
                smallest_goal_diff = goal_diff
                football_team = team_name

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
