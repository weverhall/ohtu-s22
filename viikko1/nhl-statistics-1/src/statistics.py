from player_reader import PlayerReader
from enum import Enum


def sort_by_points(player):
    return player.points

def sort_by_goals(player):
    return player.goals

def sort_by_assists(player):
    return player.assists

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class Statistics:
    def __init__(self, reader=PlayerReader):
        self._reader = reader
        self._players = self._reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
            )

        return list(players_of_team)

    def top(self, how_many, sort_by):
        if sort_by == 1:
            sorted_players = sorted(
                self._players,
                reverse=True,
                key=sort_by_points
                )

        if sort_by == 2:
            sorted_players = sorted(
                self._players,
                reverse=True,
                key=sort_by_goals
                )

        if sort_by == 3:
            sorted_players = sorted(
                self._players,
                reverse=True,
                key=sort_by_assists
                )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
