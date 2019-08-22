# '''
# Created on Jul 24, 2019
#      
# @author: daniel
# '''

# class Main(App):
#     '''
#     This class has methods for printing the output of the Reader class 
#     '''
#     read = Reader()
#      
#     def build(self):
#         self.screen = GameScreen(players=10)
#         self.screen.test(1) #we can use that principle to create labels for cards AND change em every update, yaaay
#         return self.screen
#          
#     def toWords(self,card):
#         cards=['ace','two','three','four','five','six','seven','eight','nine','ten','jack','queen','king']
#         colors = ['clubs','hearts','spades','diamonds']
#         colorIndex = ceil(card/13)-1
#         cardIndex = card - colorIndex*13 -1
#         return (cards[cardIndex]+" of " +colors[colorIndex])
#          
#     def display(self):
#         return self.toWords(self.read.lastRead())
#      
#          
# t = Main()
# t.run()
import tkinter as tk
from math import floor
from Reader import Reader
import threading
LARGE_FONT = 10
MEDIUM_FONT = 5
class App(tk.Tk):
    frames={}
    cards=[]
    reader = Reader()
    
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        
        container.pack(side="top", fill="both", expand = True)
        
        #container.grid_rowconfigure(0,weight=1) #0 - min size, weight = 1 - priority
        #container.grid_columnconfigure(0, weight=1)
        
        frame = EqualDeal(container,self,2) #set start frame
        
        self.frames[EqualDeal] = frame # the key is the id(EqualDeal) of the class apparently (according to stack overflow). 
        #pretty cool and i guess i'll stick with it
        
        
        frame.grid(row=0,column=0, sticky="nsew") #set the grid INSIDE of the frame
        print('lol')
        threading.Thread(target=self.getCards).start()
        print('xdd')
        self.cardsUpdate()
        self.changeFrame(EqualDeal)
#         self.proc = Process(target=self.getCards)
#         self.proc.start()
    def changeFrame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()
    def getCards(self):
        self.cards.append(self.reader.lastRead())
        print(self.cards)
        self.getCards()
    def cardsUpdate(self):

        frame = self.frames[EqualDeal]
        frame.updateCards(self.cards)
        print(self.cards)
        self.after(500,self.cardsUpdate)

        
    
        
        
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
        
        self.updateLabels(players)
        
#         cards=[27, 1, 27]
#         self.updateCards(cards)
     
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
        
        



myApp = App()
myApp.mainloop()





