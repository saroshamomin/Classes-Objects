#Program header goes here

#ADD ANY NECESSARY IMPORT STATEMENTS HERE
import shape, circle, square, triangle

#Define main function
def main():

    #CREATE A SHAPE: red, border (1), name: Generic Shape
    my_shape = shape.Shape("red", 1, "Generic Shape")

    #CREATE A CIRCLE: blue, border (2), name: Circle
    my_circle = circle.Circle("blue", 2, "Circle")

    #CREATE A SQUARE: yellow, border (3), name: Square
    my_square = square.Square("yellow", 3, "Square")

    #CREATE A TRIANGLE: orange, border (4), name: Triangle
    my_triangle = triangle.Triangle("orange", 4, "Triangle")

    #ADD CODE TO SET THE APPROPRIATE ATTRIBUTES OF EACH SUBCLASS:
    #CIRCLE: RADIUS = 4
    #SQUARE: SIDE = 5
    #TRIANGLE: BASE = 4, HEIGHT = 10
    my_circle.set_radius(4)
    my_square.set_side(5)
    my_triangle.set_base(4)
    my_triangle.set_height(10)

    #create a list to store shapes and print them
    shape_list = [my_shape, my_circle, my_square, my_triangle]
    
    for x in shape_list:
        print(x)
    
    for x in shape_list:
        if isinstance(x, circle.Circle):
            print("The circumference is", x.calc_circumference())
        if isinstance(x, square.Square):
            print("The perimeter is", x.calc_perimeter())
        if isinstance(x, triangle.Triangle):
            print("The area is", x.calc_area())


    #ADD CODE TO PRINT THE VALUES OF EACH SHAPE, INCLUDING SHAPE
    '''print(my_shape)
    print(my_circle)
    print(my_square)
    print(my_triangle)'''

    #ADD CODE TO PRINT THE AREA OF THE CIRCLE, SQUARE, AND TRIANGLE
    '''print("The area of the circle is", my_circle.calc_area())
    print("The area of the square is", my_square.calc_area())
    print("The area of the triangle is", my_triangle.calc_area())'''

#Call main function
main()
