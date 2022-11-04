import unittest
from statistics import Statistics
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_top_by_points(self):
        self.assertEqual(self.statistics.top(4, 1)[0].name, "Gretzky")

    def test_top_by_goals(self):
        self.assertEqual(self.statistics.top(4, 2)[0].name, "Lemieux")

    def test_top_by_assists(self):
        self.assertEqual(self.statistics.top(4, 3)[0].name, "Gretzky")

    def test_search_available_player(self):
        self.assertEqual(self.statistics.search("Yzerman").assists, 56)

    def test_search_unavailable_player(self):
        self.assertFalse(self.statistics.search("Antetokounmpo"))

    def test_team_list_frequency(self):
        self.assertEqual(len(self.statistics.team("EDM")), 3)
