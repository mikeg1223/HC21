class Intersection:

    def __init__(self, id):
        # blah
        self.waitingCars = {}
        self.outgoingStreets = {}
        self.intersectionId = id
        self.currentLight = 0
        self.lights = {}
        self.lightSchedule = {}

    def changeLight(self, streetName):
        self.lights[self.currentLight] = False
        self.currentLight = streetName
        self.lights[streetName] = True
    
    def addIncomingStreet(self, streetName): #preprocessing
        self.lights[streetName] = False
        self.waitingCars[streetName] = {}
    
    def addOutgoingStreet(self, streetName, streetCost): #preprocessing
        self.outgoingStreets[streetName] = streetCost
    
    def addIntoQueue(self, c): #during runtime
        # put a car in waitingCars{} specifically for the street
        # we get the street from c.pop from street c.pop()
        cameFromStreet = c.pop()
        self.waitingCars[cameFromStreet].append(c)
    
    def runGreenLight(self):
            return self.waitingCars[self.currentLight].pop()

    def debug(self):
        print( str("Intersection " + str(self.intersectionId) + "\n") )

