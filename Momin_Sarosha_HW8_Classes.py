#Author: Sarosha Momin
#Homework Number & Name: Return on Investment HW8
#Due Date: November 12
#Program Description: Create a class that validates the initial and current value input from user, and a 
#class that calculates the return on investment. 

class ValidationClass:              #class to validate input
    #validates input to be float
    def checkFloat(self,num):
        retry = True    #bool variable to use as flag    
        while retry:        
            try: 
                if float(num) >= 0:
                    retry = False
                elif num == '':    #checks if left blank       
                    num = -1
                if float(num) < 0:
                    retry = True
                    num = input("Enter a valid number: ")
            except Exception:     #when input is non-numbers            
                retry = True            
                num = input("Enter a valid number: ")   
        return float(num)
    
    #validates input to be integer
    def checkInteger(self, num):
        retry = True    #bool variable to use as flag    
        while retry:        
            try: 
                if int(num) >= 0:
                    retry = False
                elif num == '':    #checks if left blank               
                    num = -1
                if int(num) < 0:
                    retry = True
                    num = input("Enter a valid number: ")
            except Exception:     #when input is non-numbers            
                retry = True            
                num = input("Enter a valid number: ")   
        return int(num)
        
class CalculationClass:
    #set attributes for the CalculationClass object 
    def __init__(self):
        self.initialValue = 5
        self.currentValue = 10
        self.ROI = 2
        self.netProfit = 3
    
    #set initial and current value
    def set_InitialValue(self, value):
        self.initialValue = value
    
    def set_CurrentValue(self, value):
        self.currentValue = value
   
    #calculate the net profit and the roi
    def calculateNetProfit(self):
        self.netProfit = self.currentValue - self.initialValue
        return self.netProfit
    
    def calculateROI(self):
        self.ROI = (self.netProfit / self.initialValue) * 100
        return self.ROI
    
    #return the roi in a read-only property
    def getROI(self):
        return format(self.ROI, '.2f')

