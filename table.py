class Table:
    def __init__(self,name,partner1,partner2):
        self.name = name
        self.partners = [partner1,partner2]
    def getPartners(self):
        return self.partners
    def getName(self):
        return self.name
    def __str__(self):
        return "Table " + str(self.name)
