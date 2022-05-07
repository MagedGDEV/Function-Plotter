import tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from function import Function

 
class GUI:

    height: int
    width: int
    textWidth: int

    root: tkinter.Tk
    canvas: tkinter.Canvas

    functionTextBox: tkinter.Entry
    minTextBox: tkinter.Entry
    maxTextBox: tkinter.Entry

    messageLabel: tkinter.Label
    minLabel:tkinter.Label
    maxLabel:tkinter.Label
    functionLabel: tkinter.Label

    button: tkinter.Button

    figure: Figure
    graphCanvas : FigureCanvasTkAgg

    messageLabelDrawn = False
    graphDrawn = False
    
    def __init__ (self, canvasHeight, canvasWidth):
        
        self.height = canvasHeight
        self.width = canvasWidth
        self.guiSettings()
        self.textWidth = 200
        self.minLabel = self.addLabel(30, 20, "minX")
        self.minTextBox = self.addTextBox (75, 20 , 50)
        self.maxLabel = self.addLabel(140, 20, "maxX")
        self.maxTextBox = self.addTextBox (185, 20 , 50)
        self.functionLabel = self.addLabel (33, 50, "F(y) = ")
        self.functionTextBox = self.addTextBox(150, 50, self.textWidth)
        self.errorMessage = ""
        self.addButton(140, 100)
        self.root.mainloop()
    
    # Add label to display the error for the user if there was invalid input
    def addLabel (self, positionX, positionY, message):
        label = tkinter.Label(self.root, text = message, wraplength= self.textWidth)
        self.canvas.create_window (positionX, positionY, window= label)
        return label

    # Add button to be pressed when user enters input to display the graph
    def addButton (self, poistionX, positionY):
        self.button = tkinter.Button(text = 'Plot the input', command= self.checkUserInput)
        self.canvas.create_window(poistionX, positionY, window= self.button)
    
    # function that is going to be called when user press the button
    def checkUserInput (self):
        
        funcVerify = Function(self.functionTextBox.get(), self.minTextBox.get(), self.maxTextBox.get())
        
        if (self.messageLabelDrawn):
            self.messageLabel.destroy()
        
        if (funcVerify.errorMessage == ""):
            self.messageLabel = self.addLabel (400, 50, "Valid Input")
            self.addGraph(funcVerify.equation, int(self.minTextBox.get()), int (self.maxTextBox.get()))
            self.graphDrawn = True
        else: 
            self.messageLabel = self.addLabel (400, 50, funcVerify.errorMessage)
            if (self.graphDrawn): 
                self.graphCanvas.get_tk_widget().destroy()  
                self.graphDrawn = False
        self.messageLabelDrawn = True
        
    # Add textbox to take the user input from the user
    def addTextBox(self, positionX, positionY, textBoxWidth):
        textBox = tkinter.Entry (self.root)
        self.canvas.create_window (positionX, positionY, window= textBox, width=textBoxWidth)
        return textBox
        
    #intialize the settings of the canvas
    def guiSettings(self):
        self.root = tkinter.Tk()
        self.root.title('Function Plot')
        self.canvas = tkinter.Canvas (self.root,height= self.height,width= self.width)
        self.canvas.pack()
        
    # Add graph that plots the function entered by the user
    def addGraph (self, equation, minValue, maxValue):
        
        # to remove the old graph and create new one
        if (self.graphDrawn): 
            self.graphCanvas.get_tk_widget().destroy()

        self.figure = Figure(figsize = (10, 10),
                     dpi = 50)
        
        # evaluate the value of the function from the minimum to maximum entered
        y = []
        for x in range(minValue,maxValue + 1): 
            y.append(eval(equation))
        x = [i for i in range (minValue,maxValue + 1)]
        plot1 = self.figure.add_subplot(111)
        plot1.plot(x,y)
        self.graphCanvas = FigureCanvasTkAgg(self.figure,master = self.root)  
        self.graphCanvas.draw()
        self.graphCanvas.get_tk_widget().pack()
        self.graphCanvas.get_tk_widget().pack() 

