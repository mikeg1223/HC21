
class Street:
    
    def __init__(self,textLine, id):
        tokens = textLine.split()
        print(textLine)
        self.streetId = id
        self.startIntersectionId = tokens[0]
        self.endIntersectionId = tokens[1]
        self.name = tokens[2]
        self.cost = tokens[3]
    
    def debug(self):
        print( str("Street Name " + self.name + "   " + self.startIntersectionId + "-->"  + self.endIntersectionId + "    cost - " + self.cost + "\n") )
