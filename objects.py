class Player:
    def __init__(self, first, last, position, at_bats, hits):
        self.first = first
        self.last = last
        self.position = position 
        self.at_bats = at_bats
        self.hits = hits

    def full_name(self):
        return self.first + '' + self.last
    
    def average(self):
        average = self.hits / self.at_bats
        average = "{0:.3f}".format(average).ljust(6)
        return average
    
class Lineup:
    def __init__(self):
        self.__lineup = []
        