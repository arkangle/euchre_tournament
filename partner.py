class Partner:
    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2
    def __eq__(self,otherPartner):
        if(self.player1 == otherPartner.player1 and self.player2 == otherPartner.player2):
            return True
        elif(self.player2 == otherPartner.player1 and self.player1 == otherPartner.player2):
            return True
        else:
            return False
    def __ne__(self,otherPartner):
        return not(self.__eq__(otherPartner))
            
