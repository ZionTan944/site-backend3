import random


class SoccerMatchClient:
    def __init__(self):
        self.match_time_range = 90

    def play_match(self, match_index, home_team, away_team):
        if home_team.team_int == "RES" or away_team.team_int == "RES":
            return

        goal_range = (home_team.team_rate * 30) + (away_team.team_rate * 30)

        home_goals = 0
        away_goals = 0
        for _ in range(self.match_time_range):
            goal_sum = random.randint(0, goal_range)

            if goal_sum >= 0 and goal_sum <= away_team.team_rate:
                away_goals += 1
            elif goal_sum >= (goal_range - home_team.team_rate):
                home_goals += 1

        print(home_team, home_goals, "-", away_goals, away_team)
        home_team.record_stats(match_index, home_goals, away_goals)
        away_team.record_stats(match_index, away_goals, home_goals)

