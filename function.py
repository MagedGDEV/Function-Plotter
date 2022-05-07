from tokenize import String
import re

class Function:

    equation: String
    minValue: String
    maxValue: String
    errorMessage: String
    def __init__(self, equationTextBox, minTextBox, maxTextBox) ->None:
        
        self.equation = equationTextBox
        self.minValue = minTextBox
        self.maxValue = maxTextBox
        self.errorMessage = ""
        self.errorMessage += self.checkMin()
   
        if (self.errorMessage == ""):
            self.errorMessage += self.checkMax()
        else:
            if (self.checkMax() != ""):
                self.errorMessage += ", " + self.checkMax()
        if (self.errorMessage == ""):
            self.errorMessage += self.checkMinMax()

        if (self.errorMessage == ""):
            self.errorMessage += self.checkEquation()
        else:
            if (self.checkEquation() != ""):
                self.errorMessage += ", " + self.checkEquation()
        if (self.errorMessage == ""):
            self.equation = self.changePowerSymbol()
        
    
    def checkEquation (self):
        
        if (self.equation == ""):
            return "Enter the equation at F(y)"
        else:
            matchObj = re.match(r"(( *-? *[0-9]+ *[\+\-\/\*^] *x *)|( *x *)|( *-? *[0-9]+ *))(( *[\+\-\/\*^] *)(( *-? *[0-9]+ *[\+\-\/\*^] *x *)|( *x *)|( *-? *[0-9]+ *)))*",self.equation)
            if matchObj:
                if matchObj.group() == self.equation:
                    return ""
                else: 
                    return "Invalid equation, Please enter equation in correct forum"
            else:
                return "Invalid equation, Please enter equation in correct forum"
    # make sure input in minimum is smaller that maximum
    def checkMinMax(self):
        if (int(self.minValue) >= int(self.maxValue)):
            return "Enter value in minX smaller that the value in MaxX"
        return ""

    def checkMin(self):
        # user hasn't entered Minimum Value
        if self.minValue == "":
            return "Enter value in minX"
        elif (self.checkValue(self.minValue) == "invalid"):
            return "Invalid input in minX, please enter integer values"
        return ""
    
    def checkMax (self):
        # user hasn't entered Minimum Value
        if self.maxValue == "":
            return "Enter value in maxX"
        elif (self.checkValue(self.maxValue) == "invalid"):
            return "Invalid input in maxX, please enter integer values"
        return ""
    # make sure user entered only integer values
    def checkValue(self, value):
        
        matchObj = re.match (r"-?[0-9]*", value)
        if matchObj: 
            if (matchObj.group() == value): 
                return "value is in correct form"
        return "invalid"

    def changePowerSymbol (self):
        return self.equation.replace ("^", "**")
