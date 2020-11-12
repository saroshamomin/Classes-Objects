#Class header goes here

#ADD ANY NECESSARY IMPORT STATEMENTS HERE
import shape

#Define constants
PI = 3.14

#Define the Circle class
#UPDATE TO INHERIT FROM SHAPE
class Circle(shape.Shape):

    #Define the initializer method
    #UPDATE TO INCLUDE ARGUMENTS AND CALL INIT METHOD FROM SHAPE
    def __init__(self, color, border, name):
        #CALL INIT METHOD FROM SHAPE PASSING NECESSARY ARGUMENTS
        super().__init__(color, border, name) 
        
        #DEFINE ATTRIBUTES SPECIFIC TO CIRCLES; ASSIGN DEFAULT VALUES
        self.__radius = 4
        
    def __str__(self):
        #CREATE STRING USING __str__ FROM SUPER AND ADD RADIUS
        string = super().__str__() + ", Radius: " + str(self.__radius)
        return string

    #Create accessors
    def get_radius(self):
        return self.__radius

    #Create mutators
    def set_radius(self, new_radius):
        if new_radius > 0:
            self.__radius = new_radius
        else:
            print("Invalid radius. Radius not changed.")

    #Define calculate circumference method
    def calc_circumference(self):

        #Calculate circ
        circ = PI * 2 * self.__radius

        return circ

    #Define calc area method
    def calc_area(self):

        #Calcuate area
        area = PI * self.__radius**2

        return area
