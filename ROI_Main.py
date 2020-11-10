#Author: Sarosha Momin
#Program Description: Import the Validation and Calculation classes. Create an object to access the attributes of the class adn properly display 
#the Return on Investment to the user. 

import Momin_Sarosha_HW8_Classes

def main():
    #create an object for each class
    roi_obj = Momin_Sarosha_HW8_Classes.CalculationClass()
    value_obj = Momin_Sarosha_HW8_Classes.ValidationClass()
    
    #get initial value input from user and validate it
    initial = input("What is the initial value? ")
    initial = value_obj.checkFloat(initial)

    #get current value input from user and validate it
    current = input("What is the current value? ")
    current = value_obj.checkFloat(current)

    #set the new values to the attributes
    roi_obj.set_InitialValue(initial)
    roi_obj.set_CurrentValue(current) 
    
    #calculate net profit and roi
    roi_obj.calculateNetProfit()
    roi_obj.calculateROI() 
    
    #display the ROI
    print("The ROI for this investment is ", roi_obj.getROI(), "%", sep = '') 
    
main()
