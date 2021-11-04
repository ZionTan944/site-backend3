import random
import numpy as np
from .TableSorter import run_merge_sort

# from TableSorter import run_merge_sort

from tabulate import tabulate
from copy import deepcopy

TeamName = [
    "Chelsea",
    "Liverpool",
    "Manchester City",
    "Manchester United",
    "Everton",
    "Brighton",
    "Brentford",
    "Tottenhem",
    "West Ham United",
    "Aston Villa",
    "Arsenal",
    "Wolves",
    "Leicester City",
    "Crystal Palace",
    "Watford",
    "Leeds United",
    "Southampton",
    "Burnley",
    "Newcastle",
    "Norwich City",
]
TeamInt = [
    "CHE",
    "LIV",
    "MCI",
    "MUN",
    "EVE",
    "BHA",
    "BRE",
    "TOT",
    "WHU",
    "AVL",
    "ARS",
    "WOL",
    "LEI",
    "CRY",
    "WAT",
    "LEE",
    "SOU",
    "BUR",
    "NEW",
    "NOR",
]
# TeamRate =  [191,203,205,189,183,140,148,178,160,150,\
#     160,146,121,112,111,80,89,88,80,78]

TeamRate = [
    390,
    380,
    370,
    320,
    300,
    220,
    220,
    300,
    210,
    180,
    290,
    160,
    150,
    140,
    130,
    120,
    110,
    90,
    70,
    50,
]
Events = [
    [": Rumors of financial issues surface!", 0.9],
    [": Transer rumors for star striker rampant", 0.8],
    [": Owner pledges to go all-in this season", 1.3],
    [": Coach found at local bar during practice hours", 0.75],
    [": Player arrested for drug possession charges", 0.7],
    [": Investing fortunes into new club equipment", 1.2],
    [": Team bus gets into accident during transit", 0.6],
    [": Local fanclub invited to anniversary event", 1.1],
    [": Captain promises to stay until retirment", 1.2],
    [": New trainers coming in from overseas", 1.4],
]
# def EventChanger(self.value):
#   return lambda events : self.value * events

# self.value = myfunc(self.value)


class Team:
    def __init__(self, TeamName, TeamInt, TeamRate, TeamIndex):
        self.ScheduledGames = []
        self.LastMatches = []
        self.TeamName = TeamName
        self.TeamInt = TeamInt
        self.TeamRate = TeamRate
        self.TeamIndex = TeamIndex
        self.GP = 0
        self.Wins = 0
        self.Draws = 0
        self.Losses = 0
        self.GoalsFor = 0
        self.GoalsAgainst = 0
        self.GoalDiff = 0
        self.Points = 0
        self.Form = 40
        self.Fatigue = 0
        self.CurrentPlacing = int(TeamIndex) if TeamIndex != "N" else "N"

    def statistics_entry(self, Points, GoalsFor, GoalsAgainst):
        # Update stats for teams after matches
        self.Points += Points
        self.GoalsFor += GoalsFor
        self.GoalsAgainst += GoalsAgainst
        self.GoalDiff += GoalsFor - GoalsAgainst
        self.GP += 1
        self.Fatigue += 4
        if Points == 3:
            self.Wins += 1
            self.Form = min([int(self.Form * (1.1 + (GoalsFor // 10))), 80])
        elif Points == 1:
            self.Draws += 1
            self.Form = max([self.Form * 0.95, 15])
        else:
            self.Losses += 1
            self.Form = max([int(self.Form * (0.9 - (GoalsAgainst // 10))), 15])


class League(Team):
    def __init__(self, TeamLst, Events):
        self.Matchday = 1
        self.TeamLst = TeamLst
        self.OrgTeamLst = TeamLst
        self.MatchPlayed = []
        self.Events = Events

    def init_league(self):
        self.Fixtures = self.schedule()
        self.set_team_schedule()
        # self.start_season()

    def retrieve_team_data(self, TeamInt):
        for index in range(len(self.TeamLst)):
            if TeamInt == self.TeamLst[index].TeamInt:
                final_index = index
        return (
            self.TeamLst[final_index].TeamName,
            [
                self.TeamLst[final_index].CurrentPlacing,
                self.TeamLst[final_index].GP,
                self.TeamLst[final_index].Wins,
                self.TeamLst[final_index].Draws,
                self.TeamLst[final_index].Losses,
                self.TeamLst[final_index].GoalsFor,
                self.TeamLst[final_index].GoalsAgainst,
                self.TeamLst[final_index].GoalDiff,
                self.TeamLst[final_index].Points,
            ],
            self.TeamLst[final_index].ScheduledGames,
            self.TeamLst[final_index].LastMatches,
        )

    def set_team_schedule(self):
        for MatchWeek in self.Fixtures:
            if MatchWeek == ["Rest"]:
                for Team in self.TeamLst:
                    Team.ScheduledGames.append(
                        {
                            "oppo": "Rest",
                            "loc": None,
                            "result": None,
                        }
                    )
            else:
                for Match in MatchWeek:
                    if Match == ["N", "N"]:
                        continue
                    for Team in Match:
                        if "N" not in Match:
                            if Match[0] == Team:
                                self.TeamLst[
                                    self.TeamLst[Team].TeamIndex
                                ].ScheduledGames.append(
                                    {
                                        "loc": "Home",
                                        "result": None,
                                        "oppo": self.TeamLst[
                                            self.TeamLst[Match[1]].TeamIndex
                                        ].TeamInt,
                                    }
                                )
                            else:
                                self.TeamLst[
                                    self.TeamLst[Team].TeamIndex
                                ].ScheduledGames.append(
                                    {
                                        "loc": "Away",
                                        "result": None,
                                        "oppo": self.TeamLst[
                                            self.TeamLst[Match[0]].TeamIndex
                                        ].TeamInt,
                                    }
                                )

                        else:
                            if Team != "N":
                                self.TeamLst[
                                    self.TeamLst[Team].TeamIndex
                                ].ScheduledGames.append(
                                    {
                                        "oppo": "Rest",
                                        "loc": None,
                                        "result": None,
                                    }
                                )

    def reset_league(self):
        self.Matchday = 1
        self.TeamLst = deepcopy(self.OrgTeamLst)

    def randomise_TeamName(self):
        self.TeamLst.pop(11)
        self.TeamLst.pop(0)
        ##  Randomise list of TeamName for scheduling
        ChangesMade = 0
        while True:
            Change = random.randint(0, (len(self.TeamLst) // 2) - 1)
            ChangesMade += 1

            self.TeamLst.append(self.TeamLst[Change])
            self.TeamLst.pop(Change)

            Stop = random.randint(0, ((len(self.TeamLst)) - ChangesMade))
            if Stop == 0:
                break

    def schedule(self):
        self.randomise_TeamName()
        self.TeamLst.insert(10, Team("Rest", "RES", 0, "N"))
        self.TeamLst.insert(0, Team("Rest", "RES", 0, "N"))
        ## Generate fixtures, firstfixtures is home, secondfixtures is reveresed of firstfixtures
        FirstFixtures = []
        SecondFixtures = []
        for i in range(len(self.TeamLst) - 1):
            FirstMatches = []
            SecondMatches = []
            for count in range(len(self.TeamLst) // 2):
                FirstMatches.append(
                    [
                        self.TeamLst[count].TeamIndex,
                        self.TeamLst[count + (len(self.TeamLst) // 2)].TeamIndex,
                    ]
                )
                SecondMatches.append(
                    [
                        self.TeamLst[count + (len(self.TeamLst) // 2)].TeamIndex,
                        self.TeamLst[count].TeamIndex,
                    ]
                )

            FirstFixtures.append(FirstMatches)
            SecondFixtures.append(SecondMatches)

            self.TeamLst.insert(1, self.TeamLst[len(self.TeamLst) // 2])
            self.TeamLst.pop((len(self.TeamLst) // 2) + 1)
            self.TeamLst.append(self.TeamLst[len(self.TeamLst) // 2])
            self.TeamLst.pop((len(self.TeamLst) // 2))

        FirstWeek = FirstFixtures[0]
        LastWeek = SecondFixtures[0]
        Fixtures = FirstFixtures[1:] + SecondFixtures[1:]

        ## Randomising Fixtures
        ChangesMade = 0
        while ChangesMade < 50:
            Change = random.randint(0, (len(self.TeamLst) // 2) - 1)
            ChangesMade += 1
            Fixtures.append(Fixtures[Change])
            Fixtures.pop(Change)

        # Adding the rest weeks for fatigue management and stuff.
        # No rest in first and last week so all teams will play
        Fixtures.insert(0, FirstWeek)
        Fixtures.append(LastWeek)
        Fixtures.insert(22, ["Rest"])

        return Fixtures

    def start_season(self):
        self.MatchPlayed = []
        SortedTable = None
        # Simulate season
        if self.Matchday < ((len(self.TeamLst) * 2)):
            print("Matchweek:{}".format(self.Matchday))
            # Rest for previous week
            for Team in self.TeamLst:
                Team.Fatigue = max(Team.Fatigue - 2, 0)

            # Check if FULL REST WEEK
            if self.Fixtures[self.Matchday - 1][0] == "Rest":
                for Team in self.TeamLst:
                    Team.Fatigue = max(Team.Fatigue - 4, 0)
                Event = "Preparation week for next half of season"
            else:
                # ##Sim Weekly Matches
                #     WeekEventIndex = random.randint(0,len(self.Events)-1)
                #     EventTeamIndex = random.randint(0,len(self.TeamLst)-1)
                #     Event = None
                #     if self.TeamLst[EventTeamIndex].TeamName != "Rest":
                #         self.TeamLst[EventTeamIndex].Form = int(self.TeamLst[EventTeamIndex].Form * self.Events[WeekEventIndex][1])
                #         Event = self.TeamLst[EventTeamIndex].TeamName + self.Events[WeekEventIndex][0]

                for Matches in self.Fixtures[self.Matchday - 1]:
                    # Check if team is supposed to rest
                    if Matches[0] != "N" and Matches[1] != "N":
                        TeamA = self.TeamLst[Matches[0]].TeamIndex
                        TeamB = self.TeamLst[Matches[1]].TeamIndex
                        self.play_match(TeamA, TeamB)
            SortedTable = self.set_table(self.Matchday)

            self.Matchday += 1

            return SortedTable, self.Matchday - 1, self.MatchPlayed
        return None, None, None

    def play_match(self, TeamA, TeamB):
        # Rate is calculated by rating + form + if(home)
        ScoreA, ScoreB = 0, 0
        # RateA = self.TeamLst[int(TeamA)].TeamRate - self.TeamLst[int(TeamA)].Fatigue\
        #     + self.TeamLst[int(TeamA)].Form + 40
        # RateB = self.TeamLst[int(TeamB)].TeamRate - self.TeamLst[int(TeamA)].Fatigue \
        #     + self.TeamLst[int(TeamB)].Form
        RateA = self.TeamLst[int(TeamA)].TeamRate + 20
        RateB = self.TeamLst[int(TeamB)].TeamRate
        Probability = int((RateA + RateB) * 3)
        ## Simulate individual Matches
        for match_time in range(9):
            GoalProb = random.randint(0, Probability)
            if GoalProb < RateA:
                ScoreA += 1
            if GoalProb > (Probability - RateB):
                ScoreB += 1

        print(
            self.TeamLst[int(TeamA)].TeamInt,
            ScoreA,
            ":",
            ScoreB,
            self.TeamLst[int(TeamB)].TeamInt,
        )
        self.MatchPlayed.append(
            [
                self.TeamLst[int(TeamA)].TeamInt,
                ScoreA,
                "VS",
                ScoreB,
                self.TeamLst[int(TeamB)].TeamInt,
            ]
        )

        if ScoreA > ScoreB:
            self.TeamLst[int(TeamA)].statistics_entry(3, ScoreA, ScoreB)
            self.TeamLst[int(TeamB)].statistics_entry(0, ScoreB, ScoreA)
            self.TeamLst[int(TeamA)].LastMatches.append("W")
            self.TeamLst[int(TeamB)].LastMatches.append("L")

        elif ScoreA < ScoreB:
            self.TeamLst[int(TeamB)].statistics_entry(3, ScoreB, ScoreA)
            self.TeamLst[int(TeamA)].statistics_entry(0, ScoreA, ScoreB)
            self.TeamLst[int(TeamA)].LastMatches.append("L")
            self.TeamLst[int(TeamB)].LastMatches.append("W")
        else:
            self.TeamLst[int(TeamA)].statistics_entry(1, ScoreB, ScoreA)
            self.TeamLst[int(TeamB)].statistics_entry(1, ScoreA, ScoreB)
            self.TeamLst[int(TeamA)].LastMatches.append("D")
            self.TeamLst[int(TeamB)].LastMatches.append("D")

        # League Data
        self.TeamLst[int(TeamA)].ScheduledGames[self.Matchday - 1]["result"] = [
            ScoreA,
            ScoreB,
        ]
        self.TeamLst[int(TeamB)].ScheduledGames[self.Matchday - 1]["result"] = [
            ScoreB,
            ScoreA,
        ]

    def set_table(self, GamesPlayed):
        Table = []
        Table = self.TeamLst[1:11] + self.TeamLst[12:]
        ## Merge Sort for table
        SortedDict = run_merge_sort(Table)
        SortedTable = []
        for TeamInd in range(len(SortedDict)):
            if (TeamInd + 1) > SortedDict[TeamInd].CurrentPlacing:
                TeamMovement = "˅"
            elif (TeamInd + 1) < SortedDict[TeamInd].CurrentPlacing:
                TeamMovement = "˄"
            else:
                TeamMovement = "="
            for TeamLstIndex in range(len(self.TeamLst)):
                if SortedDict[TeamInd].TeamName == self.TeamLst[TeamLstIndex].TeamName:
                    self.TeamLst[TeamLstIndex].CurrentPlacing = TeamInd + 1
            SortedTable.append(
                [
                    TeamInd + 1,
                    SortedDict[TeamInd].TeamInt,
                    SortedDict[TeamInd].GP,
                    SortedDict[TeamInd].Wins,
                    SortedDict[TeamInd].Draws,
                    SortedDict[TeamInd].Losses,
                    SortedDict[TeamInd].GoalsFor,
                    SortedDict[TeamInd].GoalsAgainst,
                    SortedDict[TeamInd].GoalDiff,
                    SortedDict[TeamInd].Points,
                    TeamMovement,
                ]
            )
        print(
            tabulate(
                SortedTable,
                headers=[
                    "I",
                    "Team",
                    "GP",
                    "Wins",
                    "Draws",
                    "Losses",
                    "GF",
                    "GA",
                    "GD",
                    "Points",
                    " ",
                ],
                tablefmt="orgtbl",
            )
        )
        return SortedTable


def add_rest_team():
    # Rest Teams to act as placeholder for no matches
    TeamName.insert(10, "REST")
    TeamInt.insert(10, "RES")
    TeamRate.insert(10, 0)
    TeamName.insert(0, "REST")
    TeamInt.insert(0, "RES")
    TeamRate.insert(0, 0)


TeamClassLst = []
add_rest_team()
for i in range((len(TeamName))):
    if TeamName[i] == "REST":
        TeamClassLst.append(Team(TeamName[i], TeamInt[i], TeamRate[i], "N"))
    else:
        TeamClassLst.append(Team(TeamName[i], TeamInt[i], TeamRate[i], i))

# EPL = League(TeamClassLst,Events)
# EPL.init_league()
