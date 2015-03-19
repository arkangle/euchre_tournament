class Partner:
    def __init__(self,player1,player2):
        self.players = (player1,player2)
    def getPlayers(self):
        return self.players
    def __str__(self):
        return "Partners (%s,%s)" % (self.players[0].getName(),self.players[1].getName())
