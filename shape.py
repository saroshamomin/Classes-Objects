#Class header goes here

#Define the Shape class
class Shape:

    #Define the initializer method
    def __init__(self, new_color, new_border, new_name):
        #define attributes of each Shape object with starting values
        #Make sure border is positive before setting the border value
        self.__color = new_color
        self.__border = new_border
        self.__name = new_name

    #Create accessors
    def get_border(self):
        return self.__border

    def get_color(self):
        return self.__color

    def get_name(self):
        return self.__name

    def __str__(self):
        string = self.__name + ", Color: " + self.__color + ", Border: " + str(self.__border)
        return string
