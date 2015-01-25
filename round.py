class Round:
    def __init__(self):
        self.tables = []
        pass
    def addTable(self,table):
        self.tables.append(table)
    def getTables(self):
        return self.tables
