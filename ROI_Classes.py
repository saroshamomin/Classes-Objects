#Author: Sarosha Momin
#Program Description: Create a class that validates the initial and current value input from user, and a class that calculates the return on investment. 

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
        self.__initialValue = 5
        self.__currentValue = 10
        self.__ROI = 2
        self.__netProfit = 3
    
    #set initial and current value
    def set_InitialValue(self, value):
        self.__initialValue = value
    
    def set_CurrentValue(self, value):
        self.__currentValue = value
   
    #calculate the net profit and the roi
    def calculateNetProfit(self):
        self.__netProfit = self.__currentValue - self.__initialValue
        return self.__netProfit
    
    def calculateROI(self):
        self.__ROI = (self.__netProfit / self.__initialValue) * 100
        return self.__ROI
    
    #return the roi in a read-only property
    def getROI(self):
        return format(self.__ROI, '.2f')

