class Controls:
    def __init__(self):
        self.content = ''
        return

    def show(self):
        return self.content
    
    def setPrompt(self, title, message, options: dict):
        self.content = "\n  __"+str(title).upper()+"__\n\n"
        self.content = self.content + "  " + message + "\n\n"
        for x in options:
            self.content = self.content + "  [ "
            self.content = self.content + str(x) + " ] "
            self.content = self.content + str(options[x])
        self.content = self.content + "  [ "
        self.content = self.content + "Q ] "
        self.content = self.content + "Quit"
        return
        