import os
from view.Header import Header
from view.Display import Display
from view.Controls import Controls

class View:
    def __init__(self):
        self.header = Header("Rack-O")
        self.display = Display()
        self.controls = Controls()
        return
    
    def refresh(self):
        os.system('cls')
        print(self.header.show())
        print(self.display.show())
        print(self.controls.show())
        return input()
    
    def transition(self, message):
        os.system('cls')
        content = "\n\n  "+str(message).upper()+"\n\n  press any key to continue"
        print(self.header.show())
        print(content)
        input()
        
    
    def getDisplay(self):
        return self.display
    
    def getControls(self):
        return self.controls
        