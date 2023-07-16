import itertools


def generate_fixtures_table(teams):
    num_teams = len(teams)
    num_rounds = num_teams - 1
    matches_per_round = num_teams // 2

    fixtures_table = []
    rounds = []

    for round in range(num_rounds):
        round_fixtures = []
        for i in range(matches_per_round):
            home = teams[i]
            away = teams[num_teams - 1 - i]
            home_city, home_stadium = get_city_and_stadium(home)
            away_city, away_stadium = get_city_and_stadium(away)
            leg = "1" if round % 2 == 0 else "2"

            fixture = [home, home_city, "vs",
                       away, away_city, home_stadium, leg]
            round_fixtures.append(fixture)

        rounds.append(round_fixtures)
        teams.insert(1, teams.pop())

    # Generate the second leg fixtures
    second_leg_fixtures = [[fixture[3], fixture[4], "vs", fixture[0],
                            fixture[1], fixture[5], "2"] for fixture in rounds[0]]
    rounds.append(second_leg_fixtures)

    fixtures_table = list(itertools.chain(*rounds))
    return fixtures_table


def get_city_and_stadium(team):
    # Replace this with your own logic to retrieve the city and stadium for each team
    teams_info = {
        "OstrichAssociates": ("Nakuru", "Oassociates"),
        "Nakuru FC": ("Nakuru", "Nakuru Field"),
        "Mavuno Comrades FC": ("Thika", "Vuno Grounds"),
        "Lake Basin FC": ("Kisumu", "Lbasin"),
        "Sharks United": ("Kisumu", "Sharks Field"),
        "Sea Horses FC": ("Mombasa", "Shorses Arena"),
        "Dolphins FC": ("Mombasa", "Dolphins"),
        "Wolves FC": ("Nairobi", "Wolves"),
        "Cklein Stars": ("Nairobi", "Cklein Arena")
    }

    return teams_info.get(team, ("", ""))


# List of teams in the tournament
teams = ["OstrichAssociates", "Nakuru FC", "Mavuno Comrades FC", "Lake Basin FC",
         "Sharks United", "Sea Horses FC", "Dolphins FC", "Wolves FC", "Cklein Stars"]

# Generate the fixtures table
fixtures_table = generate_fixtures_table(teams)

# Print the fixtures table
print("| Home               | City        | vs | Away           | City           | Stadium       | Leg |")
print("|--------------------|-------------|----|----------------|----------------|---------------|-----|")
for fixture in fixtures_table:
    print("| {:<19} | {:<12} | {} | {:<14} | {:<14} | {:<13} | {}  |".format(*fixture))

