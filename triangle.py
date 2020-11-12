#Class header goes here

#ADD ANY NECESSARY IMPORT STATEMENTS HERE
import shape

#Define the Triange class
#UPDATE TO INHERIT FROM SHAPE
class Triangle(shape.Shape):

    #Define the initializer method
    #UPDATE TO INCLUDE ARGUMENTS AND CALL INIT METHOD FROM SHAPE
    def __init__(self, color, border, name):
        #CALL INIT METHOD FROM SHAPE PASSING NECESSARY ARGUMENTS
        super().__init__(color, border, name)
        
        #DEFINE ATTRIBUTES SPECIFIC TO TRIANGLES; ASSIGN DEFAULT VALUES
        self.__height = 4
        self.__base = 2
        
    def __str__(self):
        #CREATE STRING USING __str__ FROM SUPER AND ADD BASE AND HEIGHT
        string = super().__str__() + ", Base: " + str(self.__base) + ", Height: " + str(self.__height)
        return string

    #Create accessor
    def get_base(self):
        return self.__base

    #Create mutator
    def set_base(self, new_base):
        if new_base > 0:
            self.__base = new_base
        else:
            print("Invalid base. Base not changed.")

    #Create accessor
    def get_height(self):
        return self.__height

    #Create mutator
    def set_height(self, new_height):
        if new_height > 0:
            self.__height = new_height
        else:
            print("Invalid height. Height not changed.")

    #Define calc area method
    def calc_area(self):

        #Calcuate area
        area = 0.5 * self.__base * self.__height

        return area
