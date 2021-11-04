class SoccerTeam:
    def __init__(self, team_name, team_int, team_rate, team_index):
        self.scheduled_games = []
        self.team_name = team_name
        self.team_int = team_int
        self.team_rate = team_rate
        # index without rest teams
        self.team_index = team_index
        self.games_played = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.goals_for = 0
        self.goals_against = 0
        self.goal_difference = 0
        self.points = 0


class SoccerLeague:
    def __init__(self, team_lst):
        self.Matchday = 1
        self.TeamLst = team_lst
