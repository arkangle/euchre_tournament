import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    def testGetName(self):
        player = Player(1)
        self.assertEqual(1,player.getName())
    def testToString(self):
        player1 = Player(1)
        self.assertEqual("Player 1",str(player1))
    def testPlayWith(self):
        player1 = Player(1)
        player2 = Player(2)
        player1.playWith(player2)
        self.assertEqual(player1.playedWith,[player2])
        player2.playWith(player1)
        self.assertEqual(player2.playedWith,[player1])
    def testHasPlayedWith(self):
        player1 = Player(1)
        player2 = Player(2)
        self.assertFalse(player1.hasPlayedWith(player2))
        player1.playWith(player2)
        self.assertTrue(player1.hasPlayedWith(player2))
