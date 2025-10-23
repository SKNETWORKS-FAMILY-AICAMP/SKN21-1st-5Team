'''
작성자: 김가람
날짜: 2025-10-22
'''
from dataclasses import dataclass

class DriverData:
    def __init__(self, name, team, country, img = ""):
        self.name = name
        self.team = team
        self.country = country
        self.img = img

@dataclass
class Statistic:
    def __init__(self, 
                 name: str,
                 season_position: int,
                 season_points: int,
                 grand_prix_races: int,
                 grand_prix_points: int,
                 grand_prix_wins: int,
                 grand_prix_podiums: int,
                 grand_prix_poles: int,
                 grand_prix_top_10s: int,
                 dhl_fastest_laps: int,
                 dnfs: int,
                 sprint_races: int,
                 sprint_points: int,
                 sprint_wins: int,
                 sprint_podiums: int,
                 sprint_poles: int,
                 sprint_top_10s: int):
        self.name = name
        self.season_position = season_position
        self.season_points = season_points
        self.grand_prix_races = grand_prix_races
        self.grand_prix_points = grand_prix_points
        self.grand_prix_wins = grand_prix_wins
        self.grand_prix_podiums = grand_prix_podiums
        self.grand_prix_poles = grand_prix_poles
        self.grand_prix_top_10s = grand_prix_top_10s
        self.dhl_fastest_laps = dhl_fastest_laps
        self.dnfs = dnfs
        self.sprint_races = sprint_races
        self.sprint_points = sprint_points
        self.sprint_wins = sprint_wins
        self.sprint_podiums = sprint_podiums
        self.sprint_poles = sprint_poles
        self.sprint_top_10s = sprint_top_10s

