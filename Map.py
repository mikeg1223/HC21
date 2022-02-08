from Intersection import Intersection
from Street import Street
from Car import Car

class Map:

    def __init__(self):
        self.preprocessing("./in/a.txt")
        self.printEverything()

    def preprocessing(self, fileName):
        extracted = []
        inp_file = open(fileName)
        
            # read input file
        lineNumber = 0
        streetLines = {}
        carsLines = {}

        for line in inp_file:
            split_line = line.split()
            if (lineNumber == 0):
                extracted = (split_line)
                self.duration = extracted[0]
                self.num_intersections = int(extracted[1]) #
                self.num_streets = int(extracted[2]) #
                self.num_cars = int(extracted[3]) #
                self.bonus_pts = int(extracted[4]) #
                lineNumber+=1
            else:
                if lineNumber <= self.num_streets: # if we are reading streets
                    streetLines[lineNumber-1] = line
                    
                else:
                    carsLines[lineNumber-self.num_streets-1] = line
                lineNumber+=1

            #create all intersections
        self.intersections = {}
        for i in range(self.num_intersections):
            num = Intersection(i)
            self.intersections[str(i)] = num  #hashmap of intersection ID --> this class intersection

            #create all streets
        self.streets = {}    #list of streets in class form
        for s in range(self.num_streets):
            st = Street( streetLines[s], s )
            self.streets[st.name] = st   #hashmap of its name --> this class instance
            self.intersections[st.startIntersectionId].debug()
            self.intersections[st.startIntersectionId].addOutgoingStreet(st.name, st.cost)
            self.intersections[st.endIntersectionId].addIncomingStreet(st.name)

            #create all cars    
        self.cars = {}
        for c in range(self.num_cars):
            ca = Car(str(carsLines[c]), c)
            self.cars[c] = ca
    

    def printEverything(self):
        for i in self.intersections:
            i.debug()
        
        for s in self.streets:
            s.debug()
        
        for c in self.cars:
            c.debug()
        

    # program runs from below 
if __name__ == "__main__":
    m = Map()