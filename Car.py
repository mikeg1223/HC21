class Car:

    def __init__(self, textLine,id):
        # Constructor
        self.carId = id
        tokens = textLine.split()
        self.numStreets = tokens[0]
        self.pathRemaining = tokens[1:]

    def pop(self):
        # Function to remove the latest street (front of list) from cars path
        self.numStreets -= 1
        return self.pathRemaining.pop(0)

    def isDone(self):
        return not self.pathRemaining


    def debug(self):
        print(str("Car Paths Remaining -- " + self.pathRemaining ))