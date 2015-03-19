import unittest
from round import Round
from player import Player
from partner import Partner
from table import Table

class TestRound(unittest.TestCase):
    def getTable(self,table_name,name1,name2,name3,name4):
        player1 = Player(name1)
        player2 = Player(name2)
        player3 = Player(name3)
        player4 = Player(name4)
        partner1 = Partner(player1,player2)
        partner2 = Partner(player3,player4)
        return Table(table_name,partner1,partner2)
    def testAddTable(self):
        round1 = Round()
        table1 = self.getTable("T1","P1","P2","P3","P4")
        table2 = self.getTable("T2","P5","P6","P7","P8")
        round1.addTable(table1)
        round1.addTable(table2)
        tables = round1.getTables()
        self.assertEqual(table1,tables[0])
        self.assertEqual(table2,tables[1])
