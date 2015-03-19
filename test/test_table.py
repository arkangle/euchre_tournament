import unittest
from player import Player
from partner import Partner
from table import Table

class TestTable(unittest.TestCase):
    def setUp(self):
        player1 = Player("bob")
        player2 = Player("sue")
        partner1 = Partner(player1,player2)
        player3 = Player("ralph")
        player4 = Player("greg")
        partner2 = Partner(player3,player4)
        self.table = Table("Awesome",partner1,partner2) 
    def testGetName(self):
        name = self.table.getName()
        self.assertEqual("Awesome",name)
    def testToString(self):
        strung = str(self.table)
        self.assertEqual("Table Awesome",strung)
    def testGetPartners(self):
        partners = self.table.getPartners()
        self.assertEqual("Partners (bob,sue)",str(partners[0]))
        self.assertEqual("Partners (ralph,greg)",str(partners[1]))
