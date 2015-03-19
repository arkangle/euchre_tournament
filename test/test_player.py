import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    def testGetName(self):
        player = Player(1)
        self.assertEqual(1,player.getName())
    def testToString(self):
        player1 = Player(1)
        self.assertEqual("Player 1",str(player1))
