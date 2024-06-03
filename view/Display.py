class Display:
    def __init__(self):
        self.discard = list()
        self.content = dict()
        return
    
    def show(self):
        output = ""
        if 'player' in self.content.keys():
            output = output + self.content['player']
        if 'rack' in self.content.keys():
            output = output + self.content['rack']
        if 'discard' in self.content.keys():
            output = output + self.content['discard']
        return output
    
    def setPlayer(self, player):
        self.content['player'] = '\n  __PLAYER '+str(player)+'__\n\n'
        
    def setRack(self, rack):
        content = "  Index    Card\n"
        i = 1
        for x in rack.view():
            content = content + "  " + str(i)
            if i < 10:
                content = content + " "
            content = content + "       "
            content = content + str(x) + "\n"
            i = i + 1
        self.content['rack'] = content
        
    def setDiscard(self, discard):
        self.discard = discard
        
    def updateDiscard(self):
        content = '\n\n'
        if len(self.discard) == 0:
            content = content + '  DISCARD EMPTY \n\n'
        else:
            content = content + '  DISCARD '+str(self.discard[-1])+'\n\n'
            # if len(self.discard) > 1:
            #     x = 0
            #     if len(self.discard) >= 5:
            #         x = 4
            #     elif len(self.discard) > 1:
            #         x = len(self.discard) - 1
            #     content = content + '  PREVIOUS '
            #     if x > 1:
            #         content = content +str(x)+' DISCARDS:  '
            #     else:
            #         content = content + 'DISCARD: '
            #     i = 0
            #     while i < x:
            #         content = content + str(self.discard[-i])
            #         if x - i > 1:
            #             content = content + ','
            #         i = i + 1
            #     content = content + " "
        self.content['discard'] = content
        
    