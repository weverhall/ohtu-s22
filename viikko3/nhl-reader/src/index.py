from stats import PlayerStats
from reader import PlayerReader
from datetime import datetime


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    print("Players from FIN " + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "\n")

    for player in players:
        print(player)

main()
