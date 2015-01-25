import unittest
from player import Player
from partner import Partner

class TestPartner(unittest.TestCase):
    def testEqual(self):
        player1 = Player(1)
        player2 = Player(2)
        partner1 = Partner(player1,player2)
        partner2 = Partner(player1,player2)
        partner3 = Partner(player2,player1)
        self.assertEqual(partner1,partner2)
        self.assertEqual(partner3,partner2)
        self.assertEqual(partner1,partner3)
    def testNotEqual(self):
        player1 = Player(1)
        player2 = Player(2)
        player3 = Player(3)
        partner1 = Partner(player1,player2)
        partner2 = Partner(player1,player3)
        partner3 = Partner(player2,player3)
        self.assertNotEqual(partner1,partner2)
        self.assertNotEqual(partner1,partner2)
        self.assertNotEqual(partner1,partner3)
