import unittest
from player import Player
from partner import Partner

class TestPartner(unittest.TestCase):
    def setUp(self):
        player1 = Player("bob")
        player2 = Player("sue")
        self.partner = Partner(player1,player2)
    def testGetPlayers(self):
        players = self.partner.getPlayers()
        self.assertEqual(players[0].getName(),"bob")
        self.assertEqual(players[1].getName(),"sue")
    def testToString(self):
        strung = str(self.partner)
        self.assertEqual(strung,"Partners (bob,sue)")
