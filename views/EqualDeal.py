from math import floor
import tkinter as tk
MEDIUM_FONT = 10

class EqualDeal(tk.Frame):
    '''
    This is the frame(view) for games in which each player gets the same amount of cards
    
    '''
    cardLabels=[]
    labels=[]
    def __init__(self, parent, controller, players):
        self.players = players
        tk.Frame.__init__(self, parent)
        
        self.spin = tk.Spinbox(master=parent, from_=2, to=15,command=self.spinUpdate)
        self.spin.grid(pady=10,padx=100,column=2,row=0)
        self.ClearCards = tk.Button(self, text="Clear cards lol",command=controller.clearCards)
        self.ClearCards.grid(pady=10,padx=10,column=3,row=0)
        self.updateLabels(players)

    def updateCards(self,cards):
        '''
        function that takes an array of cards and assigns them to labels as if
        they were dealt in the order they are in in the array 
        '''
        i=0
        for l in self.cardLabels:
            l['text']=""
        for c in cards:
            print(c)
            if i==self.players:
                i=0
            self.cardLabels[i]['text']+=str(c)+" "
            print(self.cardLabels[i]['text'])
            #print(i)
            i+=1
            
    def updateLabels(self,players):
        '''
        takes an amount of players and makes an appropriate amount of labels for them
        '''
        players=int(players)
        for l in self.cardLabels:
            l.grid_forget()
        self.cardLabels.clear()
        
        for l in self.labels:
            l.grid_forget()
        self.labels.clear()
        
        for i in range(players):
            label = tk.Label(self,text="player"+str(i)+":",font=MEDIUM_FONT)
            cardLabel = tk.Label(self, text="cards go here ", font=MEDIUM_FONT)
            if i == 0:
                row = i*2
                col = 0
            else:
                row = floor(i/2.0)
                col = i % 2
            row = i
            label.grid(pady=10,padx=100,column=0, row=row)
            cardLabel.grid(pady=10,padx=100, column=1, row=row)
            self.cardLabels.append(cardLabel)
            self.labels.append(label)
         
    def spinUpdate(self):
        self.players=int(self.spin.get())
        self.updateLabels(self.spin.get())
        
        

