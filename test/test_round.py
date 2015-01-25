import unittest
from round import Round
from player import Player
from table import Table

class TestRound(unittest.TestCase):
    def testAddPlayer(self):
        round = Round()
        table = Table(1)
        self.assertEqual([],round.tables)
        round.addTable(table)
        self.assertEqual([table],round.tables)

