class Player:
    def __init__(self,name):
        self.name=name
        self.playedWith=[]
    def getName(self):
        return self.name
    def playWith(self,player):
        self.playedWith.append(player)
    def hasPlayedWith(self,player):
        return self.playedWith.count(player) > 0
    def __str__(self):
        return "Player " + str(self.name)
