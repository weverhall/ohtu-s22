import requests
from player import Player
from datetime import datetime


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['team'],
            player_dict['assists'],
            player_dict['goals']
        )
        if player_dict['nationality'] == 'FIN':
            players.append(player)

    print("Players from FIN " + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "\n")

    players.sort(key=lambda x: x.goals + x.assists, reverse=True)

    for player in players:
        print(player)

main()
