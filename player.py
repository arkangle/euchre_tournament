class Player:
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
    def __str__(self):
        return "Player " + str(self.name)
