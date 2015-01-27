import random
from round import Round

class Game:
    def __init__(self,tables,players):
        self.tables = tables
        self.players = players
    def getRound(self):
        player_indexes = list(range(0,len(self.players)))
        random.shuffle(player_indexes)
        round = Round()
        for Table in self.tables:
            table = Table.new()
            for p in range(0,4):
                player_index = player_indexes.pop()
                player = self.players[player_index]
                table.addPlayer(player)
            round.addTable(table)
        return round

