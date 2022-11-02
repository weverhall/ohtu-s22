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

    def test_returns_top_player(self):
        self.assertEqual(self.statistics.top(3)[0].name, "Gretzky")

    def test_search_available_player(self):
        self.assertEqual(self.statistics.search("Gretzky").assists, 89)

    def test_search_unavailable_player(self):
        self.assertFalse(self.statistics.search("Antetokounmpo"))

    def test_returns_team_size(self):
        self.assertEqual(len(self.statistics.team("EDM")), 3)
