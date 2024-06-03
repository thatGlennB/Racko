class Header:
    def __init__(self, title):
        self.title = title
        return
    
    def show(self):
        return "\n\n    ***  ***  "+str(self.title).upper()+"  ***  ***\n\n"